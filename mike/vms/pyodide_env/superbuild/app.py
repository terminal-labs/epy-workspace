import os
import yaml
import shutil
import hashlib

from cli_passthrough import cli_passthrough

def cli():
    os.chdir("/vagrant/cython")
    print("in ", os.getcwd())
    os.environ["CYTHON"] = "True"
    cli_passthrough("python setup.py build_ext --inplace")
    cli_passthrough("python setup.py sdist bdist_wheel")
    del os.environ["CYTHON"]

    with open('/vagrant/cython/dist/cythonexample-0.1.tar.gz', 'rb') as f:
        sha256_hash = hashlib.sha256()
        for byte_block in iter(lambda: f.read(4096),b""):
            sha256_hash.update(byte_block)
        hashsum = sha256_hash.hexdigest()

    d = {
        "package":
            {"name": "cythonexample", "version": "0.1"},
        'source':
            {"url": "file:///vagrant/cython/dist/cythonexample-0.1.tar.gz", "sha256": hashsum}
        }

    if not os.path.exists("/home/vagrant/pyodide/packages/cythonexample"):
        os.mkdir("/home/vagrant/pyodide/packages/cythonexample")

    if os.path.exists("/home/vagrant/pyodide/packages/cythonexample/meta.yaml"):
        os.remove("/home/vagrant/pyodide/packages/cythonexample/meta.yaml")
    with open('/home/vagrant/pyodide/packages/cythonexample/meta.yaml', 'w') as outfile:
        yaml.dump(d, outfile, default_flow_style=False)

    os.chdir("/home/vagrant/pyodide/packages/cythonexample")
    print("in ", os.getcwd())
    if os.path.exists("dist"):
        shutil.rmtree('dist')
    if os.path.exists("build"):
        shutil.rmtree('build')
    os.environ["PYTHONPATH"] = "$PYTHONPATH:/home/vagrant/pyodide/pyodide-build/"
    cli_passthrough("python -m pyodide_build buildpkg meta.yaml")

    os.chdir("/home/vagrant/pyodide")
    print("in ", os.getcwd())
    os.environ["PYODIDE_PACKAGES"] = "cythonexample"
    cli_passthrough("make")

    if os.path.exists("/home/vagrant/pyodide/build/cythonexample-0.1-cp310-cp310-emscripten_wasm32.whl"):
        os.remove("/home/vagrant/pyodide/build/cythonexample-0.1-cp310-cp310-emscripten_wasm32.whl")
    shutil.copy('packages/cythonexample/dist/cythonexample-0.1-cp310-cp310-emscripten_wasm32.whl', 'build/cythonexample-0.1-cp310-cp310-emscripten_wasm32.whl')
