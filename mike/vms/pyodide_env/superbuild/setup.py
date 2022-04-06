from setuptools import setup

setup(
    name="superbuild",
    version='0.1',
    py_modules=['app'],
    install_requires=[
        'Click',
        'cli-passthrough',
    ],
    entry_points='''
        [console_scripts]
        superbuild=app:cli
    ''',
)
