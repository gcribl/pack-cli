# Pack ID Tool

A CLI tool to modify Cribl pack IDs in `.crbl` files.

## Overview

This tool unpacks a Cribl `.crbl` file (tar.gz archive), renames the pack directory and updates the `name` field in `package.json`, then repacks it with the new ID.

## Installation

### Via Homebrew (Recommended)

```bash
brew tap yourusername/pack-id-tool
brew install pack-id-tool
```

### Via pip

```bash
pip install pack-id-tool
```

### From source

```bash
git clone https://github.com/yourusername/pack-cli.git
cd pack-cli
pip install -e .
```

## Usage

```bash
pack-id <input_file.crbl> <new_id>
```

### Example

```bash
pack-id cribl-search-sysdig.crbl my-custom-pack
```

This will:

1. Unpack `cribl-search-sysdig.crbl`
2. Rename the directory to `my-custom-pack`
3. Update the `name` field in `package.json` to `my-custom-pack`
4. Create a new file `my-custom-pack.crbl`

## Tab Completion

Tab completion is automatically installed when you install via Homebrew. It supports bash, zsh, and fish shells.

After installation, you can use tab completion:

```bash
pack-id <TAB>  # Completes .crbl files in current directory
pack-id my-file.crbl <TAB>  # Shows naming convention suggestions
```

### Naming Conventions

The tool suggests two naming conventions for pack IDs:

- **Community packs**: `cc-<product>-<tech>` (e.g., `cc-stream-deeptempo-io`)
- **Cribl official packs**: `cribl-<product>-<tech>` (e.g., `cribl-search-sysdig`)

### Manual Installation (if not using Homebrew)

**Bash:**

```bash
# Copy completion script
sudo cp completions/pack-id.bash /usr/local/etc/bash_completion.d/pack-id
# Or source it in your ~/.bashrc
source /path/to/completions/pack-id.bash
```

**Zsh:**

```bash
# Copy to a directory in your $fpath
sudo cp completions/_pack-id /usr/local/share/zsh/site-functions/
# Reload completions
compinit
```

**Fish:**

```bash
# Copy to fish completions directory
cp completions/pack-id.fish ~/.config/fish/completions/
```

After installing completions, restart your shell or source your shell configuration file.

## Features

- Preserves all file structure and contents
- Automatically excludes `.DS_Store` files (like `gtar --exclude .DS_Store`)
- Updates package.json name field
- Creates a clean output file with the new ID

## Requirements

- Python 3.7+

## License

MIT License - see LICENSE file for details
