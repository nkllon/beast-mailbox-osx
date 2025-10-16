import sys
def test_import():
    if sys.platform == "darwin":
        import beast_mailbox_osx as m
        info = m.osx_info()
        assert isinstance(info, dict)
        assert "platform" in info
