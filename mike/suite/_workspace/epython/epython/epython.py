"""
EPython is a code-transformer that translates a statically typed subset of
Python syntax into an extension of Python for a particular backend.

The .epy file is first compiled into an AST
The AST is validated to ensure it uses only the allowed subset of Python
The AST is then fed to a transformer specific to the backend.

"""
import os
from os import listdir
from os.path import isfile, join
import ast
import os.path

from epython import __version__
from .validate import validate
from .core import MyApplication

import click

def find_plugins(path):
    onlyfiles = [f for f in listdir(path) if isfile(join(path, f))]
    return onlyfiles

def main():
    pass
    # parser = argparse.ArgumentParser(prog='epython',
    #         description="Compile statically typed subset of Python to a backend.")
    # parser.add_argument("file")
    # parser.add_argument("--backend", default="cpython")
    # parser.add_argument("--name", default="none")
    # parser.add_argument("--version", action='version',
    #                     version='%(prog)s ' + __version__)
    # args = parser.parse_args()
    #
    # if args.name == 'none':
    #     name = os.path.splitext(args.file)[0]
    # else:
    #     name = args.name
    #
    # with open(args.file) as fi:
    #     source = fi.read()
    #
    # code = ast.parse(source, name, 'exec', type_comments=True)
    # result = validate(code)
    # if result is not None:
    #     raise result[0](result[1])
    #
    # try:
    #     transformer = _registry[args.backend]
    # except KeyError:
    #     raise RuntimeError(f"There is no epython backend registered for {args.backend}.")
    #
    # output = transformer(code, name)
    #
    # from .cython_backend import CythonGenerator
    # translator = CythonGenerator()
    # print(translator.visit(code))


PROJECT_NAME = "epython"
VERSION = "0.1"
context_settings = {"help_option_names": ["-h", "--help"]}

@click.group(context_settings=context_settings)
@click.version_option(prog_name=PROJECT_NAME.capitalize(), version=VERSION)
@click.pass_context
def cli(ctx):
    pass

@click.group(name="plugins")
def plugins_group():
    pass

@plugins_group.command(name="listplugins")
def listplugins_command():
    cwd = os.getcwd()
    print(find_plugins(cwd + "/plugins"))

@click.group(name="convert")
def convert_group():
    pass

@convert_group.command(name="test")
def convertfile_command():
    app = MyApplication()
    app.run()

@click.argument("filepath")
@click.option('-b', '--backend', 'backend', default="cython")
@convert_group.command(name="convertfile")
def convertfile_command(backend, filepath):
    print(backend, filepath)

@click.argument("apppath")
@click.option('-b', '--backend', 'backend', default="cython")
@convert_group.command(name="convertapp")
def convertapp_command(backend, apppath):
    print(backend, apppath)

cli.add_command(plugins_group)
cli.add_command(convert_group)
main = cli
