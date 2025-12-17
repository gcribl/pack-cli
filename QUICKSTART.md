# Quick Start Guide

## What Was Created

Your Python script has been converted into a distributable CLI tool with Homebrew support!

### Project Structure

```
pack-cli/
├── pack_id_tool/           # Main package
│   ├── __init__.py         # Package version info
│   └── cli.py              # CLI tool (your script)
├── homebrew-formula/       # Homebrew formula
│   └── pack-id-tool.rb     # Formula file
├── setup.py                # Python package config
├── README.md               # User documentation
├── LICENSE                 # MIT License
├── MANIFEST.in             # Package manifest
├── DEPLOYMENT.md           # Detailed deployment steps
└── pack-id-bandaid.py      # Original script (can be deleted)
```

## Test Locally (Right Now!)

Before publishing, test the tool on your machine:

```bash
# Install in development mode
cd /Users/gmola/pack-cli
pip3 install -e .

# Test the CLI
pack-id --help
pack-id your-file.crbl new-pack-id
```

## Publish to Homebrew (3 Simple Steps)

### Step 1: Push to GitHub

```bash
cd /Users/gmola/pack-cli

# Update setup.py first with your GitHub username!
# Edit lines 8-9 in setup.py

git init
git add .
git commit -m "Initial release: Pack ID Tool v1.0.0"
git branch -M main
git remote add origin https://github.com/YOURUSERNAME/pack-cli.git
git push -u origin main

# Create a release tag
git tag v1.0.0
git push origin v1.0.0
```

### Step 2: Get SHA256 Hash

```bash
# Download the release archive
curl -L https://github.com/YOURUSERNAME/pack-cli/archive/refs/tags/v1.0.0.tar.gz -o v1.0.0.tar.gz

# Get SHA256
shasum -a 256 v1.0.0.tar.gz

# Copy the hash output
```

### Step 3: Create Homebrew Tap

```bash
# Update the formula with your details
cd homebrew-formula
# Edit pack-id-tool.rb:
#   - Replace 'yourusername' with your GitHub username
#   - Replace 'YOUR_SHA256_HERE' with the hash from Step 2

# Create a new GitHub repo named "homebrew-pack-id-tool"
# Then:
git init
git add pack-id-tool.rb
git commit -m "Add pack-id-tool formula"
git branch -M main
git remote add origin https://github.com/YOURUSERNAME/homebrew-pack-id-tool.git
git push -u origin main
```

## Users Install With

```bash
brew install YOURUSERNAME/pack-id-tool/pack-id-tool
```

Or:

```bash
brew tap YOURUSERNAME/pack-id-tool
brew install pack-id-tool
```

## Usage

```bash
pack-id <input_file.crbl> <new_id>
```

Example:

```bash
pack-id cribl-search-sysdig.crbl my-custom-pack
```

## Alternative: PyPI Distribution

If you prefer `pip install` instead of Homebrew:

```bash
# Build and upload to PyPI
pip3 install build twine
python3 -m build
twine upload dist/*

# Users install with:
pip install pack-id-tool
```

## Need Help?

- See `DEPLOYMENT.md` for detailed instructions
- See `README.md` for user documentation

