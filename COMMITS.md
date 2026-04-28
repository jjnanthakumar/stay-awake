# Conventional Commits Guide

This project uses **Conventional Commits** for automatic semantic versioning.

## Commit Message Format

```
<type>(<scope>): <subject>

<body>

<footer>
```

## Types for Version Bumping

### Patch Release (0.0.X) - Bug Fixes
```bash
git commit -m "fix: resolve issue with mouse movement"
git commit -m "fix(gui): button not visible on small screens"
```

### Minor Release (0.X.0) - New Features
```bash
git commit -m "feat: add system tray support"
git commit -m "feat(cli): add new --quiet flag"
```

### Major Release (X.0.0) - Breaking Changes
```bash
git commit -m "feat: redesign configuration format

BREAKING CHANGE: Configuration file format has changed"
```

## Common Types

- `feat:` - New feature (bumps minor version)
- `fix:` - Bug fix (bumps patch version)
- `docs:` - Documentation only (no version bump)
- `style:` - Code style changes (no version bump)
- `refactor:` - Code refactoring (no version bump)
- `perf:` - Performance improvements (bumps patch)
- `test:` - Adding tests (no version bump)
- `chore:` - Build process or auxiliary tool changes (no version bump)
- `ci:` - CI configuration changes (no version bump)

## Examples

### Adding a New Feature
```bash
git commit -m "feat: add dark mode to GUI

Adds a toggle button for dark mode in the settings menu.
Users can now switch between light and dark themes."
```
**Result:** Version bumps from `v1.0.0` to `v1.1.0`

### Fixing a Bug
```bash
git commit -m "fix: correct mouse pattern calculation

The circle pattern was drawing incorrectly on some screen sizes.
Now uses proper scaling calculations."
```
**Result:** Version bumps from `v1.1.0` to `v1.1.1`

### Breaking Change
```bash
git commit -m "feat: switch to YAML configuration

BREAKING CHANGE: Configuration files are now in YAML format instead of JSON.
Users must convert their config.json to config.yaml."
```
**Result:** Version bumps from `v1.1.1` to `v2.0.0`

### No Version Bump
```bash
git commit -m "docs: update README with new examples"
git commit -m "chore: update dependencies"
git commit -m "style: format code with black"
```
**Result:** No version change

## Automatic Release Process

1. **Write Code**
2. **Commit with Conventional Format**
   ```bash
   git add .
   git commit -m "feat: add scheduler feature"
   ```
3. **Push to Main Branch**
   ```bash
   git push origin main
   ```
4. **GitHub Actions Automatically:**
   - Analyzes your commit messages
   - Determines version bump (major/minor/patch)
   - Creates new version tag
   - Builds executables
   - Creates GitHub release
   - Uploads binaries

## Multi-Commit Releases

When you have multiple commits:
- Latest commit type determines the bump
- `feat` + `fix` = minor bump (feat wins)
- Multiple `feat` = single minor bump
- Any `BREAKING CHANGE` = major bump (always wins)

## Best Practices

### ✅ Good Commits
```bash
feat: add circular mouse pattern
fix: resolve GUI button positioning
docs: add usage examples to README
feat(cli): add --pattern flag for mouse movement
```

### ❌ Bad Commits
```bash
update stuff
fixed bug
changes
asdf
work in progress
```

## Workflow Summary

```
Write Code → Commit (conventional) → Push → Auto Tag → Auto Build → Auto Release
```

No manual tagging needed! Just commit and push! 🚀

## Commit Message Tips

1. **Use imperative mood**: "add" not "added" or "adds"
2. **Don't capitalize first letter** of subject
3. **No period at end** of subject
4. **Keep subject under 50 characters**
5. **Separate subject from body** with blank line
6. **Explain what and why**, not how

## Reference

- [Conventional Commits Specification](https://www.conventionalcommits.org/)
- [Semantic Versioning](https://semver.org/)

---

**Remember:** Every commit to `main` branch triggers automatic versioning and release! 🎉
