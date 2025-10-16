"""
Tests for beast-mailbox-osx native functions.
"""
import sys

try:
    import pytest
except ImportError:
    pytest = None


def test_osx_info():
    """Test osx_info() returns expected structure."""
    if sys.platform != "darwin":
        if pytest:
            pytest.skip("macOS-only test")
        return
    
    from beast_mailbox_osx import osx_info
    
    info = osx_info()
    assert isinstance(info, dict), "osx_info should return a dict"
    assert "platform" in info, "Should contain 'platform' key"
    assert "arch" in info, "Should contain 'arch' key"
    assert "version" in info, "Should contain 'version' key"
    
    # Verify values
    assert info["platform"] == "Darwin", "Platform should be Darwin on macOS"
    assert info["arch"] in ["arm64", "x86_64"], f"Unexpected arch: {info['arch']}"
    assert info["version"] == "0.1.0", "Version should match package version"


def test_mailbox_index():
    """Test mailbox_index() stub function."""
    if sys.platform != "darwin":
        if pytest:
            pytest.skip("macOS-only test")
        return
    
    from beast_mailbox_osx import mailbox_index
    
    # Currently returns None (stub)
    result = mailbox_index("/tmp/test")
    assert result is None, "Stub function should return None"
    
    # Should not raise errors with various inputs
    result = mailbox_index("")
    assert result is None
    
    result = mailbox_index("/nonexistent/path")
    assert result is None


def test_module_attributes():
    """Test module has expected attributes."""
    if sys.platform != "darwin":
        if pytest:
            pytest.skip("macOS-only test")
        return
    
    import beast_mailbox_osx
    
    assert hasattr(beast_mailbox_osx, "osx_info")
    assert hasattr(beast_mailbox_osx, "mailbox_index")
    assert hasattr(beast_mailbox_osx, "__all__")
    
    # Verify __all__ contains expected exports
    assert "osx_info" in beast_mailbox_osx.__all__
    assert "mailbox_index" in beast_mailbox_osx.__all__


def test_callable():
    """Test functions are callable."""
    if sys.platform != "darwin":
        if pytest:
            pytest.skip("macOS-only test")
        return
    
    from beast_mailbox_osx import osx_info, mailbox_index
    
    assert callable(osx_info), "osx_info should be callable"
    assert callable(mailbox_index), "mailbox_index should be callable"


if __name__ == "__main__":
    # Allow running tests directly
    print("Running tests...")
    
    test_osx_info()
    print("✓ test_osx_info passed")
    
    test_mailbox_index()
    print("✓ test_mailbox_index passed")
    
    test_module_attributes()
    print("✓ test_module_attributes passed")
    
    test_callable()
    print("✓ test_callable passed")
    
    print("\nAll tests passed! ✅")

