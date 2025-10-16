"""
beast-mailbox-osx: macOS-only native extension for Beast Mailbox.
"""
from ._osxcore import osx_info, mailbox_index
__all__ = ["osx_info", "mailbox_index"]
