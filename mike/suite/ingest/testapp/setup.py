from setuptools import setup

setup(
    name="epy01a",
    version='0.0.1',
    packages=['epy01a'],
    install_requires=[
    ],
    entry_points='''
        [console_scripts]
        demo=epy01a.app:main
    ''',
)
