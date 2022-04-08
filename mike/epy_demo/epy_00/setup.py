from setuptools import setup

setup(
    name="demopack",
    version='0.1',
    packages=['demopack'],
    install_requires=[
    ],
    entry_points='''
        [console_scripts]
        demo=demopack.app:main
    ''',
)
