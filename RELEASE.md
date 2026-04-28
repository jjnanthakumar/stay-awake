# Release Process

This document describes the automatic release process for NJStayAwake.

## 🚀 Fully Automatic Releases

**No manual tagging needed!** Just commit and push with conventional commit messages.

### Steps to Create a Release

1. **Write Your Code**

2. **Commit with Conventional Format** (see [COMMITS.md](COMMITS.md))
   ```bash
   git add .
   git commit -m "feat: add new scheduler feature"
   # or
   git commit -m "fix: resolve button positioning issue"
   ```

3. **Push to Main Branch**
   ```bash
   git push origin main
   ```

4. **GitHub Actions Automatically:**
   - ✅ Analyzes commit messages
   - ✅ Determines version bump (patch/minor/major)
   - ✅ Creates new version tag
   - ✅ Builds executables for Windows, Linux, and macOS
   - ✅ Runs tests on all platforms
   - ✅ Creates GitHub release with direct download links
   - ✅ Uploads individual executables (no ZIP files!)
   - ✅ **Publishes package to PyPI automatically**
   - ✅ **Version synced across GitHub and PyPI**

5. **Monitor Build**
   - Go to: `https://github.com/jjnanthakumar/njstayawake/actions`
   - Watch the build progress
   - Check for any errors

6. **Download and Test**
   - Once complete, go to Releases page
   - Download individual executables directly
   - Test on target platforms
   - If issues found, commit fix with `fix:` message

## First-Time Setup

Before first release, set up PyPI publishing:

1. **Create PyPI Account**: [https://pypi.org](https://pypi.org)
2. **Generate API Token**: Account Settings → API tokens
3. **Add to GitHub Secrets**: 
   - Go to repository Settings → Secrets → Actions
   - Add secret: `PYPI_API_TOKEN` with your token value

See [PYPI_SETUP.md](PYPI_SETUP.md) for detailed setup instructions.

Once configured, every commit triggers both GitHub release AND PyPI publish! 🚀

## Manual Publishing

If automatic publishing fails, publish manually:

### GitHub Release

Already handled automatically, but if needed:
```bash
git tag -a v1.0.0 -m "Release v1.0.0"
git push origin v1.0.0
```

### PyPI Package

```bash
# Update version in pyproject.toml manually
# Then build and upload
python -m build
twine upload dist/*
```

See [PYPI_SETUP.md](PYPI_SETUP.md) for PyPI configuration details.

## Automatic Version Numbering

Version is determined automatically from commit messages:

- **`feat:`** commits → **Minor** bump (0.X.0) - New features
- **`fix:`** commits → **Patch** bump (0.0.X) - Bug fixes  
- **`BREAKING CHANGE:`** in message → **Major** bump (X.0.0) - Breaking changes

Examples:
```bash
# Bumps from v1.0.0 to v1.0.1
git commit -m "fix: resolve mouse pattern bug"

# Bumps from v1.0.1 to v1.1.0
git commit -m "feat: add dark mode to GUI"

# Bumps from v1.1.0 to v2.0.0
git commit -m "feat: redesign config format

BREAKING CHANGE: Config file format has changed"
```

See [COMMITS.md](COMMITS.md) for detailed commit message guide.

## Release Checklist

Before creating a release:

- [ ] All tests pass locally
- [ ] Version numbers updated
- [ ] CHANGELOG updated
- [ ] README updated if needed
- [ ] Build tested locally
- [ ] Git working directory clean
- [ ] Tag follows format `vX.Y.Z`

## Troubleshooting

### Build Fails on GitHub Actions

1. Check the Actions log for errors
2. Common issues:
   - Missing dependencies
   - Import errors
   - PyInstaller compatibility

### Release Not Created

1. Ensure tag starts with `v` (e.g., `v1.0.0`)
2. Check if workflow completed successfully
3. Verify GITHUB_TOKEN has proper permissions

### Executables Don't Work

1. Test locally first
2. Check Python version compatibility
3. Verify all dependencies included
4. Test on clean machine without Python

## GitHub Actions Workflows

### `build-release.yml`
- Triggers on: Tag push (v*), main branch push
- Builds: Windows, Linux, macOS executables
- Creates: GitHub release with all builds

### `test.yml`
- Triggers on: Every push and PR
- Tests: Python 3.8, 3.9, 3.10, 3.11
- Platforms: Windows, Linux, macOS

## Post-Release

After a successful release:

1. Announce on:
   - GitHub Discussions
   - Social media (if applicable)
   - Any relevant forums

2. Monitor for issues:
   - Watch GitHub Issues
   - Test downloads work
   - Check download counts

3. Update documentation:
   - Ensure release notes are clear
   - Add to CHANGELOG.md
   - Update any external links

## Emergency Hotfix

For critical bugs:

1. Create hotfix branch from tag
2. Fix the issue
3. Create patch version (e.g., v1.0.1)
4. Follow release process
5. Merge back to main

---

**Questions?** Open an issue on GitHub!
