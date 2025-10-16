# Contributing to beast-mailbox-osx

Thank you for your interest in contributing to beast-mailbox-osx! This document provides guidelines and instructions for contributing.

## Development Setup

### Prerequisites

- macOS 11.0 or later
- Python 3.9+
- Xcode Command Line Tools (`xcode-select --install`)
- Git

### Getting Started

1. Fork the repository on GitHub
2. Clone your fork locally:

```bash
git clone https://github.com/YOUR_USERNAME/beast-mailbox-osx.git
cd beast-mailbox-osx
```

3. Create a virtual environment:

```bash
python -m venv venv
source venv/bin/activate
```

4. Install development dependencies:

```bash
pip install -e ".[dev]"
pip install pytest black flake8 mypy
```

5. Create a feature branch:

```bash
git checkout -b feature/your-feature-name
```

## Building and Testing

### Building the Extension

```bash
# Clean build
rm -rf build/ *.egg-info
python setup.py build_ext --inplace

# Or use pip
pip install -e .
```

### Running Tests

```bash
# Run all tests
pytest tests/ -v

# Run with coverage
pytest tests/ --cov=beast_mailbox_osx --cov-report=html

# Test specific architecture
arch -arm64 pytest tests/
arch -x86_64 pytest tests/
```

### Code Quality

```bash
# Format code
black src/ tests/

# Lint
flake8 src/ tests/

# Type checking
mypy src/
```

## C Extension Guidelines

### Code Style

- Follow C17 standard
- Use clear, descriptive variable names
- Add comments for complex logic
- Include error checking for all system calls
- Clean up resources (memory, file descriptors) properly

### Example C Function

```c
static PyObject* my_function(PyObject* self, PyObject* args) {
    const char* input;
    
    // Parse arguments
    if (!PyArg_ParseTuple(args, "s", &input)) {
        return NULL;
    }
    
    // Validate input
    if (input == NULL || strlen(input) == 0) {
        PyErr_SetString(PyExc_ValueError, "Input cannot be empty");
        return NULL;
    }
    
    // Your logic here
    
    // Return result or None
    Py_RETURN_NONE;
}
```

### Memory Management

- Use `PyMem_Malloc()` and `PyMem_Free()` for memory allocation
- Always check return values
- Clean up on error paths
- Use RAII-like patterns where possible

### Python API Integration

- Use appropriate `PyArg_ParseTuple()` format strings
- Set meaningful Python exceptions on errors
- Return proper Python objects
- Handle reference counting correctly

## Pull Request Process

1. **Update Documentation**: Ensure README, docstrings, and comments are updated
2. **Add Tests**: New features must include tests
3. **Follow Code Style**: Run formatters and linters
4. **Update CHANGELOG**: Add entry under "Unreleased" section
5. **Commit Messages**: Use clear, descriptive commit messages

### Commit Message Format

```
type(scope): brief description

Detailed description if needed.

Fixes #123
```

Types: `feat`, `fix`, `docs`, `test`, `refactor`, `perf`, `chore`

### Pull Request Template

```markdown
## Description
Brief description of changes

## Motivation
Why is this change needed?

## Changes
- Item 1
- Item 2

## Testing
How was this tested?

## Checklist
- [ ] Tests added/updated
- [ ] Documentation updated
- [ ] CHANGELOG.md updated
- [ ] Code formatted and linted
- [ ] All tests pass
```

## Performance Considerations

- Profile before optimizing
- Benchmark against pure Python implementation
- Use `time` and `instruments` on macOS for profiling
- Document performance improvements in PRs

### Benchmarking Template

```python
import timeit

def benchmark():
    setup = "from beast_mailbox_osx import index"
    stmt = "index('/path/to/test')"
    
    native = timeit.timeit(stmt, setup, number=10000)
    print(f"Native: {native:.4f}s")
```

## macOS API Integration

### Guidelines

- Use well-documented, stable APIs
- Provide fallback behavior when APIs fail
- Check API availability for different macOS versions
- Handle sandboxing restrictions gracefully

### Example: FSEvents Integration

```c
#include <CoreServices/CoreServices.h>

// Check if FSEvents is available
if (&FSEventStreamCreate != NULL) {
    // Use FSEvents
} else {
    // Fallback to polling or return error
}
```

## Documentation

### Docstring Format

```python
def function_name(arg1: str, arg2: int) -> dict:
    """Brief description.
    
    Detailed description if needed.
    
    Args:
        arg1: Description of arg1
        arg2: Description of arg2
    
    Returns:
        Description of return value
    
    Raises:
        ValueError: When input is invalid
    
    Example:
        >>> function_name("test", 42)
        {'result': 'success'}
    """
```

### C Documentation

```c
/**
 * Brief description.
 *
 * Detailed description if needed.
 *
 * @param self Module object (unused)
 * @param args Python tuple of arguments
 * @return Python object or NULL on error
 *
 * @note Special considerations
 * @warning Important warnings
 */
static PyObject* function_name(PyObject* self, PyObject* args) {
    // Implementation
}
```

## Questions or Issues?

- Open an issue for bugs or feature requests
- Tag issues appropriately (`bug`, `enhancement`, `question`, etc.)
- Be respectful and constructive
- Search existing issues before creating new ones

## License

By contributing, you agree that your contributions will be licensed under the MIT License.

