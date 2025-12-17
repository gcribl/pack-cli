# Fix: Command Not Found

The `pack-id` command is installed but not in your shell's PATH.

## Run These Commands in Your Terminal

```bash
# Add to your PATH permanently
echo 'export PATH="$HOME/Library/Python/3.9/bin:$PATH"' >> ~/.zshrc

# Reload your shell configuration
source ~/.zshrc

# Now test it
pack-id --help
```

## Alternative: Test Immediately (Without Reloading Shell)

```bash
# Set PATH for current session only
export PATH="$HOME/Library/Python/3.9/bin:$PATH"

# Test it
pack-id --help
```

## If You're Using Bash Instead of Zsh

```bash
echo 'export PATH="$HOME/Library/Python/3.9/bin:$PATH"' >> ~/.bash_profile
source ~/.bash_profile
```

## Verify Installation Location

```bash
which pack-id
# Should show: /Users/gmola/Library/Python/3.9/bin/pack-id

ls -la ~/Library/Python/3.9/bin/pack-id
# Should show the executable
```

## Usage After PATH is Fixed

```bash
pack-id <input_file.crbl> <new_id>

# Example:
pack-id cribl-criblvision-for-stream.crbl my-custom-pack
```

