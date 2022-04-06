from setuptools import setup
from Cython.Build import cythonize

setup(
    name='cypack',
    version='0.1',
    packages=['cypack'],
    ext_modules=cythonize("cypack/fib.pyx"),
)
