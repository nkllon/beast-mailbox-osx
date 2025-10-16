# Changelog

All notable changes to beast-mailbox-osx will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.1.0] - 2025-10-16

### Added
- Initial scaffold with universal2 C extension support
- `osx_info()` function for platform sanity checks
- `index()` stub for future macOS-specific mailbox operations
- Universal binary support (ARM64 + x86_64) for macOS 11+
- Basic test suite for import validation
- CI/CD ready with cibuildwheel configuration

### Notes
- This is a prototype/scaffold release
- Native FSEvents and macOS APIs integration planned for future releases
- Designed to be used as optional dependency via `pip install beast-mailbox-core[osx]`

