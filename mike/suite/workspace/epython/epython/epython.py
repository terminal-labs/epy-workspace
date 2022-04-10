"""
EPython is a code-transformer that translates a statically typed subset of
Python syntax into an extension of Python for a particular backend.

The .epy file is first compiled into an AST
The AST is validated to ensure it uses only the allowed subset of Python
The AST is then fed to a transformer specific to the backend.

"""
import argparse
import ast
import os.path

from epython import __version__
from .validate import validate

# See https://greentreesnakes.readthedocs.io/en/latest/nodes.html

_registry = {}

def register_func(name_or_func):
    if isinstance(name_or_func, str):
        name = name_or_func
        func = None
    else:
        func = name_or_func
        name = func.__name__
    if func is None:
        def decorator(new_func):
            _registry[name] = new_func
            return new_func
        return decorator
    else:
        _registry[name] = func
        return func

# A transformation function needs to take as agruments
#  ast: the validated ast of the code
#  filename: the name to generate the artefacts
#
# It returns the PATH (or URL) of the created artefact

@register_func('cpython')
def transform(ast, name):
    return name + '.so'

# @register_func
# def pypy(mine):
#     return mine

def main():
    find_backends()
    parser = argparse.ArgumentParser(prog='epython',
            description="Compile statically typed subset of Python to a backend.")
    parser.add_argument("file")
    parser.add_argument("--backend", default="cpython")
    parser.add_argument("--name", default="none")
    parser.add_argument("--version", action='version',
                        version='%(prog)s ' + __version__)
    args = parser.parse_args()

    if args.name == 'none':
        name = os.path.splitext(args.file)[0]
    else:
        name = args.name

    with open(args.file) as fi:
        source = fi.read()

    code = ast.parse(source, name, 'exec', type_comments=True)
    result = validate(code)
    if result is not None:
        raise result[0](result[1])

    try:
        transformer = _registry[args.backend]
    except KeyError:
        raise RuntimeError(f"There is no epython backend registered for {args.backend}.")

    output = transformer(code, name)

    from .cython_backend import CythonGenerator
    translator = CythonGenerator()
    print(translator.visit(code))


# importing the backend should be sufficient to call the decorator(s)
# that registers the function in _registry which is why the
# dictionary created here is not returned or seemingly unused.
def find_backends():
    import importlib
    import pkgutil

    # importing the module registers the function.
    discovered_plugins = {
        name: importlib.import_module(name)
        for finder, name, ispkg in pkgutil.iter_modules()
                if name.startswith('epython-')
    }

    if len(discovered_plugins) > len(_registry):
        print("Registry: ")
        print(_registry)
        print("\n\nPlugin Modules Found: ")
        print(discovered_plugins)
        raise (ValueError, "The number of Plugin Modules Found is larger "
               "than the number of transformations successfully registered.")


if __name__ == "__main__":
    code = main()
