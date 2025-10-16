# Integration Example: Using beast-mailbox-osx with beast-mailbox-core

## Current Status

✅ **Optional dependency configured** in `beast-mailbox-core/pyproject.toml`  
⏳ **Code integration pending** - Ready for future implementation

## Installation

### For Users

```bash
# Install beast-mailbox-core with macOS optimizations
pip install "beast-mailbox-core[osx]"

# Or install separately
pip install beast-mailbox-core
pip install beast-mailbox-osx  # Only on macOS
```

### For Developers

```bash
# Clone both repos
git clone https://github.com/nkllon/beast-mailbox-core.git
git clone https://github.com/nkllon/beast-mailbox-osx.git

# Install core with OSX extras
cd beast-mailbox-core
pip install -e ".[osx,dev]"
```

## Integration Pattern

### Detection Pattern (Recommended)

Add this to `beast-mailbox-core/src/beast_mailbox_core/__init__.py`:

```python
# Optional macOS native extensions
try:
    from beast_mailbox_osx import osx_info, mailbox_index
    _HAS_OSX_EXTENSIONS = True
    _OSX_INFO = osx_info()
except ImportError:
    _HAS_OSX_EXTENSIONS = False
    _OSX_INFO = None

# Export for users
__all__ = [
    "RedisMailbox",
    # ... existing exports ...
]

# Optionally export OSX availability
def has_native_osx_support():
    """Check if macOS native extensions are available."""
    return _HAS_OSX_EXTENSIONS
```

### Usage in RedisMailbox

Example integration in `beast-mailbox-core/src/beast_mailbox_core/redis_mailbox.py`:

```python
class RedisMailbox:
    def __init__(self, *args, **kwargs):
        # ... existing init ...
        
        # Use native OSX extensions if available
        if _HAS_OSX_EXTENSIONS:
            logger.info(f"Using macOS native extensions: {_OSX_INFO}")
            self._use_native_osx = True
        else:
            self._use_native_osx = False
    
    async def _index_mailbox(self, path: str):
        """Index mailbox contents (with optional native acceleration)."""
        if self._use_native_osx:
            # Use native macOS indexing (when implemented)
            from beast_mailbox_osx import mailbox_index
            result = mailbox_index(path)
            if result is not None:
                return result
        
        # Fallback to Python implementation
        return await self._index_mailbox_python(path)
```

## Example: Platform Detection

```python
#!/usr/bin/env python3
"""Example: Detect and use macOS extensions"""

def main():
    from beast_mailbox_core import RedisMailbox
    
    # Check if native extensions are available
    try:
        from beast_mailbox_osx import osx_info
        info = osx_info()
        print(f"✅ macOS extensions available!")
        print(f"   Platform: {info['platform']}")
        print(f"   Arch: {info['arch']}")
        print(f"   Version: {info['version']}")
    except ImportError:
        print("ℹ️  macOS extensions not available (cross-platform mode)")
    
    # Use mailbox normally - it will auto-detect and use native features
    mailbox = RedisMailbox(redis_url="redis://localhost:6379")
    print("Mailbox created successfully!")

if __name__ == "__main__":
    main()
```

## Testing Integration

### Test in beast-mailbox-core

Add to `beast-mailbox-core/tests/test_osx_integration.py`:

```python
"""Test macOS native extensions integration."""
import sys
import pytest

@pytest.mark.skipif(sys.platform != "darwin", reason="macOS-only test")
def test_osx_extensions_available():
    """Test that OSX extensions can be imported on macOS."""
    try:
        from beast_mailbox_osx import osx_info, mailbox_index
        info = osx_info()
        
        assert isinstance(info, dict)
        assert "platform" in info
        assert info["platform"] == "Darwin"
        assert "arch" in info
        assert info["arch"] in ["arm64", "x86_64"]
        
        # Test stub function
        result = mailbox_index("/tmp/test")
        assert result is None  # Currently a stub
        
    except ImportError:
        pytest.skip("beast-mailbox-osx not installed")

def test_cross_platform_fallback():
    """Test that core works without OSX extensions."""
    # Should work even if beast-mailbox-osx is not installed
    from beast_mailbox_core import RedisMailbox
    
    # This should not raise ImportError
    mailbox = RedisMailbox(redis_url="redis://localhost:6379")
    assert mailbox is not None
```

## Future Enhancements (v0.2.0+)

When FSEvents and native APIs are implemented:

```python
# In beast-mailbox-core
async def watch_mailbox_changes(self, path: str, callback):
    """Watch for mailbox changes with native FSEvents (macOS)."""
    if _HAS_OSX_EXTENSIONS:
        from beast_mailbox_osx import watch_directory
        
        # Use native FSEvents for ultra-fast change detection
        stream = watch_directory(path)
        # ... handle events ...
    else:
        # Fallback to polling or watchdog
        await self._watch_mailbox_polling(path, callback)
```

## Performance Benefits

When fully implemented, beast-mailbox-osx will provide:

| Operation | Python | Native OSX | Speedup |
|-----------|--------|------------|---------|
| Directory watching | Polling (slow) | FSEvents | ~100x |
| File metadata | stat() calls | Native APIs | ~10x |
| Large mailbox scan | Pure Python | C extension | ~5-10x |

## Compatibility Matrix

| Platform | beast-mailbox-core | beast-mailbox-osx | Status |
|----------|-------------------|-------------------|--------|
| macOS 11+ | ✅ Required | ✅ Recommended | Full featured |
| macOS <11 | ✅ Required | ❌ Not supported | Basic features |
| Linux | ✅ Required | N/A | Basic features |
| Windows | ✅ Required | N/A | Basic features |

## Documentation

Update `beast-mailbox-core/README.md`:

```markdown
## Installation

### Basic Installation
\`\`\`bash
pip install beast-mailbox-core
\`\`\`

### macOS Optimizations (Recommended for macOS users)
\`\`\`bash
pip install "beast-mailbox-core[osx]"
\`\`\`

This installs native macOS extensions for:
- Faster file system monitoring (FSEvents)
- Native credential storage (Keychain) - Coming in v0.3.0
- Desktop notifications - Coming in v0.3.0
```

## Summary

✅ **Current State:**
- Optional dependency configured in pyproject.toml
- Users can install with: `pip install "beast-mailbox-core[osx]"`
- Ready for code integration when native features are implemented

⏳ **Next Steps:**
1. Implement FSEvents integration in beast-mailbox-osx v0.2.0
2. Add detection code to beast-mailbox-core
3. Use native fast paths when available
4. Maintain cross-platform compatibility

🎯 **Goal:**
Seamless integration where macOS users automatically get performance benefits without changing their code.

