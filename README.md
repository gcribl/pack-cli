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

## Features

- Preserves all file structure and contents
- Automatically excludes `.DS_Store` files (like `gtar --exclude .DS_Store`)
- Updates package.json name field
- Creates a clean output file with the new ID

## Requirements

- Python 3.7+

## License

MIT License - see LICENSE file for details

