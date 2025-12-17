# Deployment Instructions

## Prerequisites

1. Create a GitHub repository for this project
2. Update `setup.py` with your actual details:
   - `author` and `author_email`
   - `url` (GitHub repo URL)

## Steps to Deploy via Homebrew

### 1. Push to GitHub

```bash
cd /Users/gmola/pack-cli
git init
git add .
git commit -m "Initial commit: Pack ID Tool v1.0.0"
git branch -M main
git remote add origin https://github.com/yourusername/pack-cli.git
git push -u origin main
```

### 2. Create a Release on GitHub

```bash
git tag v1.0.0
git push origin v1.0.0
```

Or create a release via GitHub web interface:
- Go to your repository
- Click "Releases" → "Create a new release"
- Tag version: `v1.0.0`
- Release title: `v1.0.0`
- Description: Initial release
- Publish release

### 3. Get SHA256 Hash

```bash
# Download the release tarball
curl -L https://github.com/yourusername/pack-cli/archive/refs/tags/v1.0.0.tar.gz -o v1.0.0.tar.gz

# Calculate SHA256
shasum -a 256 v1.0.0.tar.gz
```

### 4. Update Homebrew Formula

Edit `homebrew-formula/pack-id-tool.rb`:
- Replace `yourusername` with your GitHub username
- Replace `YOUR_SHA256_HERE` with the actual SHA256 hash from step 3

### 5. Create Homebrew Tap Repository

Create a new GitHub repo named `homebrew-pack-id-tool` (must start with `homebrew-`)

```bash
cd homebrew-formula
git init
git add pack-id-tool.rb
git commit -m "Add pack-id-tool formula"
git branch -M main
git remote add origin https://github.com/yourusername/homebrew-pack-id-tool.git
git push -u origin main
```

### 6. Users Can Now Install

```bash
brew tap yourusername/pack-id-tool
brew install pack-id-tool
```

Or in one command:

```bash
brew install yourusername/pack-id-tool/pack-id-tool
```

## Testing Locally Before Publishing

### Test the package installation

```bash
cd /Users/gmola/pack-cli
pip install -e .
pack-id --help
```

### Test the Homebrew formula locally

```bash
brew install --build-from-source homebrew-formula/pack-id-tool.rb
```

## Updating the Formula for New Releases

1. Update version in `setup.py` and `pack_id_tool/__init__.py`
2. Commit and push changes
3. Create new tag and release
4. Update the Homebrew formula:
   - Update `url` with new version
   - Update `sha256` with new hash
5. Commit and push formula changes

## Alternative: Publish to PyPI (pip install)

If you want users to install via `pip`:

```bash
# Build the package
python setup.py sdist bdist_wheel

# Upload to PyPI (requires account at pypi.org)
pip install twine
twine upload dist/*
```

Then users can install with:

```bash
pip install pack-id-tool
```

