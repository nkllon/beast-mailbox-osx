# Setting Up GitHub Repository

This guide will help you push this repository to GitHub as `nkllon/beast-mailbox-osx`.

## Prerequisites

- GitHub account with access to the `nkllon` organization (or create it there)
- GitHub CLI installed (`gh`) or git configured with GitHub credentials

## Option 1: Using GitHub CLI (Recommended)

```bash
# Navigate to the repository
cd /Volumes/lemon/cursor/beast-mailbox-osx

# Authenticate with GitHub (if not already done)
gh auth login

# Create the repository on GitHub
gh repo create nkllon/beast-mailbox-osx \
  --public \
  --source=. \
  --description="macOS-native extensions for Beast Mailbox (universal2 C extension)" \
  --push

# That's it! The repository is now on GitHub
```

## Option 2: Manual Setup via GitHub Web Interface

### Step 1: Create Repository on GitHub

1. Go to https://github.com/nkllon
2. Click "New repository"
3. Repository name: `beast-mailbox-osx`
4. Description: `macOS-native extensions for Beast Mailbox (universal2 C extension)`
5. Select "Public"
6. **DO NOT** initialize with README, .gitignore, or license (we already have these)
7. Click "Create repository"

### Step 2: Push to GitHub

```bash
# Navigate to the repository
cd /Volumes/lemon/cursor/beast-mailbox-osx

# Add the remote
git remote add origin https://github.com/nkllon/beast-mailbox-osx.git

# Or if using SSH:
git remote add origin git@github.com:nkllon/beast-mailbox-osx.git

# Push the code
git branch -M main
git push -u origin main
```

## Post-Setup Configuration

### 1. Enable GitHub Actions

GitHub Actions should be automatically enabled. Verify by going to:
- https://github.com/nkllon/beast-mailbox-osx/actions

### 2. Configure Branch Protection (Optional but Recommended)

1. Go to repository Settings → Branches
2. Add rule for `main` branch:
   - ✓ Require pull request reviews before merging
   - ✓ Require status checks to pass before merging
   - ✓ Require branches to be up to date before merging
   - Select: Build and Test workflow

### 3. Set up PyPI Publishing (When Ready)

1. Go to https://pypi.org/ and create an account
2. Generate an API token
3. Add to GitHub repository secrets:
   - Name: `PYPI_API_TOKEN`
   - Value: your PyPI token

### 4. Add Repository Topics

Add topics to help discovery:
- `macos`
- `native-extension`
- `python`
- `c-extension`
- `universal-binary`
- `beast-mailbox`
- `fsevents`

### 5. Update Repository Settings

**About Section:**
- Website: Link to documentation when available
- Topics: Add relevant topics (see above)

**Options:**
- ✓ Issues
- ✓ Wikis (if you want documentation wiki)
- ✓ Discussions (optional, for community)

## Verify Everything Works

After pushing, verify:

1. **Repository Structure**: Check all files are present
   ```bash
   gh repo view nkllon/beast-mailbox-osx
   ```

2. **GitHub Actions**: Should start running automatically
   ```bash
   gh run list --repo nkllon/beast-mailbox-osx
   ```

3. **Clone Test**: Try cloning in a different location
   ```bash
   cd /tmp
   git clone https://github.com/nkllon/beast-mailbox-osx.git
   cd beast-mailbox-osx
   make build
   make test
   ```

## Next Steps

1. **Create First Release**:
   ```bash
   gh release create v0.1.0 \
     --repo nkllon/beast-mailbox-osx \
     --title "v0.1.0 - Initial Scaffold" \
     --notes "See CHANGELOG.md for details"
   ```

2. **Update beast-mailbox-core**: Add this as an optional dependency:
   ```toml
   [project.optional-dependencies]
   osx = ["beast-mailbox-osx>=0.1.0; sys_platform == 'darwin'"]
   ```

3. **Publish to PyPI** (when ready):
   - Build wheels: `make wheel`
   - Test on TestPyPI first
   - Then publish to PyPI via release workflow

## Troubleshooting

### Authentication Issues

```bash
# For HTTPS, update credentials
git config credential.helper store

# For SSH, add your key
ssh-add ~/.ssh/id_rsa
gh ssh-key add ~/.ssh/id_rsa.pub
```

### Push Rejected

```bash
# Force push if needed (only safe on first push)
git push -u origin main --force
```

### CI/CD Not Running

- Check .github/workflows/build.yml is present
- Ensure GitHub Actions is enabled in repository settings
- Check workflow file for syntax errors

## Resources

- [GitHub CLI Documentation](https://cli.github.com/)
- [cibuildwheel Documentation](https://cibuildwheel.readthedocs.io/)
- [PyPI Publishing Guide](https://packaging.python.org/guides/publishing-package-distribution-releases-using-github-actions-ci-cd-workflows/)

