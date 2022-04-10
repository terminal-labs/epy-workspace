import os
import sys
import importlib

def import_path(path):
    module_name = os.path.basename(path).replace('-', '_')
    spec = importlib.util.spec_from_loader(
        module_name,
        importlib.machinery.SourceFileLoader(module_name, path)
    )
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    sys.modules[module_name] = module
    return module

mod = import_path('/home/user/Desktop/epython/epy-workspace/mike/epy_demo/epy01a/epy01a/functions.txt')

hello_world = mod.hello_world
fib = mod.fib
