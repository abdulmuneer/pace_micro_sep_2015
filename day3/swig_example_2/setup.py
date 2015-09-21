from distutils.core import setup, Extension

extension_mod = Extension("_swigdemo", ["_swigdemo_module.cc", "hello.c"])

setup(name = "swigdemo", ext_modules=[extension_mod])

