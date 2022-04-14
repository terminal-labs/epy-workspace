import os
from setuptools import setup, Extension

# Set local env var CYTHON = True if working with Cython backend
# Assumes (for now) pyodide if not CYTHON
CYTHON = bool(os.environ.get("CYTHON", False))

if CYTHON:
    from Cython.Build import cythonize  # noqa

    setup(
        name='epy03',
        version='0.0.1',
        packages=['epy03'],
        ext_modules=cythonize("epy03/functions.pyx"),
    )
else:
    setup(
        name='epy03',
        version='0.0.1',
        packages=['epy03'],
        ext_modules = [Extension(name = "epy03.functions", sources = ["epy03/functions.c"])]
    )
