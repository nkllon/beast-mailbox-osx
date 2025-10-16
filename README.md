# beast-mailbox-osx

macOS-native extensions for [Beast Mailbox](https://github.com/nkllon/beast-mailbox-core) providing platform-specific optimizations and integrations.

[![Build Status](https://github.com/nkllon/beast-mailbox-osx/workflows/Build%20and%20Test/badge.svg)](https://github.com/nkllon/beast-mailbox-osx/actions)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## Overview

This package provides **universal2** C extensions for macOS (Darwin) that accelerate mailbox operations and enable platform-specific integrations. It is designed to be installed as an optional dependency from `beast-mailbox-core`.

### Key Features

- **Universal Binary**: ARM64 + x86_64 support in a single wheel
- **macOS 11+**: Optimized for modern macOS versions
- **Native APIs**: Leverages macOS-specific APIs for optimal performance
- **Zero Dependencies**: Pure C extension with minimal overhead
- **Drop-in Enhancement**: Automatically used by beast-mailbox-core when installed

## Installation

### From PyPI (when published)

```bash
# Install beast-mailbox-core with macOS optimizations
pip install "beast-mailbox-core[osx]"

# Or install directly
pip install beast-mailbox-osx
```

### From Source

```bash
# Clone the repository
git clone https://github.com/nkllon/beast-mailbox-osx.git
cd beast-mailbox-osx

# Build and install
pip install -e .
```

## Usage

The extension is automatically detected and used by `beast-mailbox-core`. You can verify the installation:

```python
from beast_mailbox_osx import osx_info

print(osx_info())
# Output: {'platform': 'darwin', 'arch': 'arm64', 'version': '0.1.0'}
```

## Building Universal Wheels

To build universal2 wheels (for distribution or testing):

```bash
# Install build tools
pip install -U build cibuildwheel

# Build wheels
python -m cibuildwheel --output-dir dist

# The resulting wheel will work on both Intel and Apple Silicon Macs
```

## Architecture

### Native Functions

- **`osx_info()`**: Returns platform information for sanity checks
- **`index(path)`**: (Planned) Fast path for mailbox indexing using FSEvents
- **Future**: Integration with macOS Notification Center, Keychain, and other native APIs

### Build Configuration

- **Compiler**: Clang with C17 standard
- **Optimization**: `-O3` for maximum performance
- **Architectures**: Universal2 (arm64 + x86_64)
- **Minimum macOS**: 11.0 (Big Sur)

## Development

### Prerequisites

- macOS 11.0 or later
- Python 3.9+
- Xcode Command Line Tools

### Setup Development Environment

```bash
# Clone the repo
git clone https://github.com/nkllon/beast-mailbox-osx.git
cd beast-mailbox-osx

# Create virtual environment
python -m venv venv
source venv/bin/activate

# Install in development mode
pip install -e ".[dev]"

# Run tests
pytest tests/
```

### Testing

```bash
# Run tests
pytest tests/ -v

# Test on both architectures (if on Apple Silicon)
arch -arm64 python -m pytest tests/
arch -x86_64 python -m pytest tests/
```

## Roadmap

### Version 0.2.0 (Planned)
- FSEvents integration for efficient mailbox monitoring
- Native file locking using macOS APIs
- Performance benchmarks vs. pure Python implementation

### Version 0.3.0 (Planned)
- macOS Notification Center integration
- Keychain integration for secure credential storage
- Spotlight integration for message search

### Future
- Metal-accelerated message processing (if applicable)
- CoreML integration for intelligent message routing
- Native macOS app bundle support

## Contributing

Contributions are welcome! Please see [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Related Projects

- [beast-mailbox-core](https://github.com/nkllon/beast-mailbox-core) - Core Redis-backed mailbox utilities
- [beast-mode](https://github.com/nkllon/beast-mode) - Parent project

## Acknowledgments

- Built with [cibuildwheel](https://cibuildwheel.readthedocs.io/) for reliable wheel building
- Inspired by native extensions in projects like `uvloop` and `orjson`

---

**Note**: This is currently a scaffold/prototype. Native API integrations are in active development.
