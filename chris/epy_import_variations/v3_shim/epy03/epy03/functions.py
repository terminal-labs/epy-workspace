import importlib.machinery
from pathlib import Path

# Project base directory
BASE_DIR = Path(__file__).resolve().parent

# Load non-.py file
source_file = str(BASE_DIR / "functions.epy")
loader = importlib.machinery.SourceFileLoader("functions", source_file)
module = loader.load_module()

# Set variables = methods from functions source file
hello_world = module.hello_world
fib = module.fib
