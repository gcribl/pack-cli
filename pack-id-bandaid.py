import tarfile
import json
import os
import shutil
import sys

def modify_and_repackage_crbl(input_file_path, new_id):
    """
    Unpacks a .crbl file, modifies the directory name and package.json 'name' field,
    and then repacks it into a new .crbl file.

    Args:
        input_file_path (str): The path to the source .crbl file (e.g., 'original.crbl').
        new_id (str): The new ID to use for the directory name, package name,
                      and the final output file name (e.g., 'my-new-bundle').
    """

    # --- 1. Define Paths and Create a Temporary Directory ---
    temp_dir_base = f"temp_crbl_work_{os.getpid()}"
    output_file_path = f"{new_id}.crbl"

    # Ensure the output file doesn't already exist to prevent accidental overwrite
    if os.path.exists(output_file_path):
        print(f"Error: Output file '{output_file_path}' already exists.")
        return

    # Create a temporary working directory
    try:
        os.makedirs(temp_dir_base)
    except OSError as e:
        print(f"Error creating temporary directory: {e}")
        return

    print(f"Starting process for '{input_file_path}' with new ID: '{new_id}'")
    
    # --- 2. Unpack the .crbl file ---
    print("2. Extracting .crbl file...")
    # Create a directory to hold the extracted contents
    # The crbl file contains files/dirs at root level (no wrapper directory)
    # so we extract into a directory that we'll later rename
    extract_dir = os.path.join(temp_dir_base, "extracted")
    new_dir_path = os.path.join(temp_dir_base, new_id)
    
    try:
        os.makedirs(extract_dir)
        # Tar files are usually compressed (tar.gz), so 'r:gz' mode is used
        with tarfile.open(input_file_path, 'r:gz') as tar:
            tar.extractall(path=extract_dir)
    except tarfile.TarError as e:
        print(f"Error unpacking tar.gz file: {e}")
        shutil.rmtree(temp_dir_base) # Clean up
        return
    except FileNotFoundError:
        print(f"Error: Input file not found at '{input_file_path}'")
        shutil.rmtree(temp_dir_base) # Clean up
        return
    except OSError as e:
        print(f"Error creating extraction directory: {e}")
        shutil.rmtree(temp_dir_base)
        return

    # --- 3. Rename the Extracted Directory ---
    print(f"3. Renaming directory to '{new_id}'...")
    try:
        os.rename(extract_dir, new_dir_path)
    except OSError as e:
        print(f"Error renaming directory: {e}")
        shutil.rmtree(temp_dir_base)
        return

    # --- 4. Edit package.json ---
    package_json_path = os.path.join(new_dir_path, 'package.json')
    print(f"4. Updating 'name' field in '{package_json_path}'...")
    
    if not os.path.exists(package_json_path):
        print(f"Warning: 'package.json' not found at '{package_json_path}'. Skipping JSON edit.")
    else:
        try:
            # Read the JSON file
            with open(package_json_path, 'r') as f:
                data = json.load(f)

            # Modify the 'name' field
            data['name'] = new_id
            
            # Write the JSON file back
            with open(package_json_path, 'w') as f:
                json.dump(data, f, indent=4) # Use indent for readability
            print(f"   Successfully set 'name' field to '{new_id}'.")

        except (IOError, json.JSONDecodeError) as e:
            print(f"Error processing package.json: {e}")
            shutil.rmtree(temp_dir_base)
            return

    # --- 5. Repackage the new directory ---
    print(f"5. Repackaging contents into '{output_file_path}'...")
    original_cwd = os.getcwd()
    try:
        # Use 'w:gz' mode for write/gzip compression
        # Similar to: gtar -cvz --exclude .DS_Store -f ../output.crbl .
        # We cd into the directory and pack its CONTENTS (not the directory itself)
        
        # Create a filter function to exclude .DS_Store files
        def exclude_ds_store(tarinfo):
            # Exclude .DS_Store files (can be in any directory)
            if os.path.basename(tarinfo.name) == '.DS_Store':
                return None
            return tarinfo
        
        # Change to the new_id directory (where the contents are)
        os.chdir(new_dir_path)
        
        # Create the tar.gz file with contents at root level
        output_full_path = os.path.join(original_cwd, output_file_path)
        with tarfile.open(output_full_path, 'w:gz') as tar:
            # Add all items in current directory (contents, not the directory wrapper)
            for item in os.listdir('.'):
                tar.add(item, arcname=item, filter=exclude_ds_store)
        
        print(f"✅ Success! New file created: {output_file_path}")

    except tarfile.TarError as e:
        print(f"Error repackaging tar.gz file: {e}")
        # Clean up is done in the finally block
    except OSError as e:
        print(f"An OS error occurred during repackaging: {e}")
    finally:
        # Ensure we're back in the original directory before cleanup
        try:
            os.chdir(original_cwd)
        except OSError:
            pass  # Ignore errors if we're already there
        
        # --- 6. Cleanup ---
        print("6. Cleaning up temporary directory...")
        temp_dir_full_path = os.path.join(original_cwd, temp_dir_base)
        if os.path.exists(temp_dir_full_path):
            shutil.rmtree(temp_dir_full_path)
        print("   Cleanup complete.")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python script_name.py <input_file.crbl> <new_id>")
        print("Example: python script_name.py cribl-search-old.crbl my-new-pack")
        sys.exit(1)

    input_file = sys.argv[1]
    new_id_name = sys.argv[2]
    
    modify_and_repackage_crbl(input_file, new_id_name)
