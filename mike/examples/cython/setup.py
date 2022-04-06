from setuptools import setup
from Cython.Build import cythonize

setup(
    name='cythonexample',
    version='0.1',
    packages=['cythonexample'],
    ext_modules=cythonize("cythonexample/fib.pyx"),
)
