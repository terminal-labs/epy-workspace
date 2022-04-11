import os
import sys
import importlib
import importlib.util
class MyApplication:
    # We are going to receive a list of plugins as parameter
    def __init__(self, plugins:list=[]):
        # Checking if plugin were sent
        # If no plugin were set we use our default
        cwd = os.getcwd()
        spec = importlib.util.spec_from_file_location('default',cwd + "/plugins/default.py")
        module = importlib.util.module_from_spec(spec)
        sys.modules['default'] = module
        spec.loader.exec_module(module)
        module.Plugin().process(5,3)

        self._plugins = ["mod"]

    def run(self):
        cwd = os.getcwd()
        sys.path.insert(0, cwd + "/plugins/test.zip")
        from unparse import Unparser
        print("Starting my application")
        print("-" * 10)
        print("This is my core system")

        # We is were magic happens, and all the plugins are going to be printed
        for plugin in self._plugins:
            print("test")

        print("-" * 10)
        print("Ending my application")
        print()
