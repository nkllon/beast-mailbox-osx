from setuptools import setup, Extension

cflags = [
    "-O3", "-std=c17", "-fvisibility=hidden",
    "-arch", "arm64", "-arch", "x86_64",
]

ext_modules = [
    Extension(
        "beast_mailbox_osx._osxcore",
        sources=["src/beast_mailbox_osx/_osxcore.c"],
        extra_compile_args=cflags,
    ),
]

setup(ext_modules=ext_modules)
