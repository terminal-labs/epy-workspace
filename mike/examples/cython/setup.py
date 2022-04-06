import os
from setuptools import setup, Extension

# Set local env var CYTHON = True if working with Cython backend
# Assumes (for now) pyodide if not CYTHON
CYTHON = bool(os.environ.get("CYTHON", False))

if CYTHON:
    from Cython.Build import cythonize  # noqa

    setup(
        name='cythonexample',
        version='0.1',
        packages=['cythonexample'],
        ext_modules=cythonize("cythonexample/fib.pyx"),
    )
else:
    setup(
        name='cythonexample',
        version='0.1',
        packages=['cythonexample'],
        ext_modules = [Extension(name = "cypack.fib", sources = ["cypack/fib.c"])]
    )
