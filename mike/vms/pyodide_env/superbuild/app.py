import os
import yaml
import shutil
import hashlib

from cli_passthrough import cli_passthrough

def remove(path):
    if os.path.exists(path):
        if os.path.isfile(path):
            os.remove(path)
        if os.path.isdir(path):
            shutil.rmtree(path)

def cythonexample(packagename):
    appdir = "/vagrant/cython"
    appversion = "0.1"
    src_tarball = appdir + '/dist/' + packagename + '-' + appversion + '.tar.gz'
    whl = packagename + '-' + appversion + "-cp310-cp310-emscripten_wasm32.whl"

    pyodidehome = "/home/vagrant/pyodide"
    package = pyodidehome + "/packages/" + packagename
    metadata = pyodidehome + "/packages/" + packagename + "/meta.yaml"

    os.chdir(appdir)
    os.environ["CYTHON"] = "True"
    cli_passthrough("python setup.py build_ext --inplace")
    cli_passthrough("python setup.py sdist bdist_wheel")
    del os.environ["CYTHON"]

    with open(src_tarball, 'rb') as f:
        sha256_hash = hashlib.sha256()
        for byte_block in iter(lambda: f.read(4096),b""):
            sha256_hash.update(byte_block)
        hashsum = sha256_hash.hexdigest()

    d = {
        "package":
            {"name": packagename, "version": appversion},
        'source':
            {"url": "file://" + src_tarball, "sha256": hashsum}
        }

    if not os.path.exists(package):
        os.mkdir(package)

    if os.path.exists(metadata):
        os.remove(metadata)
    with open(metadata, 'w') as outfile:
        yaml.dump(d, outfile, default_flow_style=False)

    os.chdir(package)
    remove("dist")
    remove("build")
    os.environ["PYTHONPATH"] = "$PYTHONPATH:/home/vagrant/pyodide/pyodide-build/"
    cli_passthrough("python -m pyodide_build buildpkg meta.yaml")

    os.chdir(pyodidehome)
    os.environ["PYODIDE_PACKAGES"] = packagename
    cli_passthrough("make")

    remove(pyodidehome + "/build/" + whl)
    shutil.copy(pyodidehome + '/packages/' + packagename + '/dist/' + whl, pyodidehome + '/build/')

def cli():
    cythonexample('cythonexample')
