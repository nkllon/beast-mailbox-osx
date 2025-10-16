# PyPI Setup Guide for beast-mailbox-osx

## Quick Start

### 1. Create PyPI Account

**Option A: Test on TestPyPI First (Recommended)**
- Go to: https://test.pypi.org/account/register/
- Create an account
- Verify your email

**Option B: Production PyPI**
- Go to: https://pypi.org/account/register/
- Create an account
- Verify your email

### 2. Generate API Token

**For TestPyPI:**
1. Go to: https://test.pypi.org/manage/account/token/
2. Click "Add API token"
3. Name: `beast-mailbox-osx-upload`
4. Scope: "Entire account" or specific project
5. Copy the token (starts with `pypi-...`)

**For PyPI:**
1. Go to: https://pypi.org/manage/account/token/
2. Same steps as above

### 3. Configure Credentials

Create `~/.pypirc`:

```ini
[distutils]
index-servers =
    pypi
    testpypi

[pypi]
username = __token__
password = pypi-YOUR-TOKEN-HERE

[testpypi]
repository = https://test.pypi.org/legacy/
username = __token__
password = pypi-YOUR-TESTPYPI-TOKEN-HERE
```

**Or** use environment variables:
```bash
export TWINE_USERNAME=__token__
export TWINE_PASSWORD=pypi-YOUR-TOKEN-HERE
```

### 4. Test Upload to TestPyPI

```bash
cd /Volumes/lemon/cursor/beast-mailbox-osx

# Upload to TestPyPI
python3 -m twine upload --repository testpypi dist/*

# Test installation from TestPyPI
pip install --index-url https://test.pypi.org/simple/ beast-mailbox-osx
```

### 5. Upload to Production PyPI

```bash
cd /Volumes/lemon/cursor/beast-mailbox-osx

# Check the package first
python3 -m twine check dist/*

# Upload to PyPI
python3 -m twine upload dist/*

# Verify
pip install beast-mailbox-osx
python3 -c "from beast_mailbox_osx import osx_info; print(osx_info())"
```

## Current Status

✅ Wheel built: `beast_mailbox_osx-0.1.0-cp39-cp39-macosx_10_9_universal2.whl`  
✅ GitHub release created: v0.1.0  
⏳ **Next:** Upload to PyPI

## Automated Publishing via GitHub Actions

Once you have your PyPI token:

1. Add secret to GitHub:
   ```bash
   gh secret set PYPI_API_TOKEN
   # Paste your PyPI token when prompted
   ```

2. Future releases will auto-publish when you create a GitHub release!

## Notes

- For v0.1.0, we only built the wheel for Python 3.9 locally
- GitHub Actions will build wheels for Python 3.9-3.12 on future releases
- Once uploaded, you cannot delete versions from PyPI (choose wisely!)
- TestPyPI is a good practice run before production

## Verification Steps

After publishing:

```bash
# Install from PyPI
pip install beast-mailbox-osx==0.1.0

# Verify it works
python3 << EOF
from beast_mailbox_osx import osx_info, mailbox_index
print("Platform info:", osx_info())
print("Functions imported successfully!")
EOF
```

## Troubleshooting

**"Invalid or non-existent authentication"**
- Check your token is correct
- Ensure you're using `__token__` as username, not your PyPI username

**"File already exists"**
- Version 0.1.0 already uploaded (cannot re-upload same version)
- Bump version in `pyproject.toml` and rebuild

**"This filename has already been used"**
- PyPI doesn't allow re-uploading the same filename
- You must create a new version

