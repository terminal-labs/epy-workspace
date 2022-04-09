import os
from setuptools import setup, Extension

CYTHON = os.environ.get("CYTHON", False)

if CYTHON:
    from Cython.Build import cythonize  # noqa
    setup(
        ext_modules=cythonize("epy01/functions.pyx"),
        name="epy01",
        version='0.0.1',
        packages=['epy01'],
        install_requires=[
        ],
        entry_points='''
            [console_scripts]
            demo=epy01.app:main
        ''',
    )
else:

    setup(
        ext_modules=[Extension("epy01.functions", ["epy01/functions.c"])],
        name="epy01",
        version='0.0.1',
        packages=['epy01'],
        install_requires=[
        ],
        entry_points='''
            [console_scripts]
            demo=epy01.app:main
        ''',
    )
