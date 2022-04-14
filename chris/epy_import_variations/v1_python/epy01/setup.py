from setuptools import setup

setup(
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
