# PyPI Publishing Instructions for v0.1.0

## ✅ Current Status

- ✅ Wheel built and verified: `beast_mailbox_osx-0.1.0-cp39-cp39-macosx_10_9_universal2.whl`
- ✅ GitHub release created: https://github.com/nkllon/beast-mailbox-osx/releases/tag/v0.1.0
- ✅ Package passes twine validation
- ⏳ **Awaiting PyPI credentials**

## 🔑 Setup PyPI Credentials

### Option 1: Add to ~/.env (Your Preferred Method)

Add these lines to your `~/.env` file:

```bash
# PyPI Publishing
export TWINE_USERNAME=__token__
export TWINE_PASSWORD=pypi-YOUR_ACTUAL_TOKEN_HERE
```

Get your token:
1. Go to https://pypi.org/account/register/ (create account if needed)
2. Go to https://pypi.org/manage/account/token/
3. Click "Add API token"
4. Name: `beast-mailbox-osx`
5. Scope: "Entire account" (or specific to project after first upload)
6. Copy the token (starts with `pypi-`)

### Option 2: Or use ~/.pypirc

```ini
[pypi]
username = __token__
password = pypi-YOUR_ACTUAL_TOKEN_HERE
```

## 📦 Publish to PyPI

Once credentials are configured:

```bash
cd /Volumes/lemon/cursor/beast-mailbox-osx

# Source your environment
source ~/.env

# Upload to PyPI
python3 -m twine upload dist/beast_mailbox_osx-0.1.0-cp39-cp39-macosx_10_9_universal2.whl

# Wait for processing (usually < 1 minute)

# Verify it's live
pip install beast-mailbox-osx==0.1.0
python3 -c "from beast_mailbox_osx import osx_info; print(osx_info())"
```

## 🤖 Setup GitHub Actions Auto-Publishing

For future releases to auto-publish to PyPI:

```bash
cd /Volumes/lemon/cursor/beast-mailbox-osx

# Add PyPI token to GitHub secrets
gh secret set PYPI_API_TOKEN
# Paste your PyPI token when prompted
```

Then future releases will automatically:
1. Build wheels for Python 3.9-3.12
2. Run tests on all versions
3. Publish to PyPI when a release is created

## ⚠️ Important Notes

- **First upload:** You can only upload each version once. If it fails, you must bump the version.
- **Package name reservation:** Once uploaded, the name `beast-mailbox-osx` is yours on PyPI.
- **Wheel format:** This wheel is only for Python 3.9. GitHub Actions will build for 3.9-3.12.
- **No deletion:** PyPI doesn't allow deleting releases (only "yanking" them).

## 🧪 Optional: Test on TestPyPI First

If you want to test before publishing to production:

```bash
# Upload to TestPyPI
python3 -m twine upload --repository-url https://test.pypi.org/legacy/ dist/*

# Test install
pip install --index-url https://test.pypi.org/simple/ beast-mailbox-osx
```

## 📝 Post-Publishing Checklist

After publishing to PyPI:

- [ ] Verify package appears at: https://pypi.org/project/beast-mailbox-osx/
- [ ] Test installation: `pip install beast-mailbox-osx`
- [ ] Update beast-mailbox-core to include as optional dependency
- [ ] Announce release (if applicable)

## 🆘 Troubleshooting

**"Invalid or non-existent authentication"**
- Double-check token is correct
- Ensure using `__token__` as username (not your PyPI username)
- Token should start with `pypi-`

**"File already exists"**
- Version 0.1.0 already uploaded
- Cannot re-upload same version
- Must bump version in `pyproject.toml` and rebuild

---

**Ready to publish?** Run the commands above once you've added your PyPI token to `~/.env`!

