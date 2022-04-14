import os
from setuptools import setup, Extension

# Set local env var CYTHON = True if working with Cython backend
# Assumes (for now) pyodide if not CYTHON
CYTHON = bool(os.environ.get("CYTHON", False))

if CYTHON:
    from Cython.Build import cythonize  # noqa

    setup(
        name='epy02',
        version='0.0.1',
        packages=['epy02'],
        ext_modules=cythonize("epy02/functions.pyx"),
    )
else:
    setup(
        name='epy02',
        version='0.0.1',
        packages=['epy02'],
        ext_modules = [Extension(name = "epy02.functions", sources = ["epy02/functions.c"])]
    )
