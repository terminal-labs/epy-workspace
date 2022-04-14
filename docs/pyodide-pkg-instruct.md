- `git clone epython` && `cd /epython` && `pip install -e .`
  (this puts `epython` cli cmd in path)
- cd into pyodide && `pip install -e pyodide-build` (uses local copy included /w pyodide)
- May also need to run `pip install -e .` from pyodide root dir
  (check into this)

Choose one of the two following sections:

# a. Pure python pkg:

- cd into pkg
- `python setup.py sdist bdist_wheel`

# b. .epy pkg:

- ensure that the package's setup file uses the bifurcated
  setup() function
- `export CTYHON=True`
- `python setup.py build_ext --inplace` (makes .c file(s))
- `python setup.py sdist bdist_wheel` (makes `/dist` files)
- `unset CYTHON`

# Final instructions:

- rename shim.py to _shim.py (subbing name of actual shim file)
- Get sha256sum of pkg source code /dist/\<pkg stuff>.tar.gz
  and make note of it's filesystem location
- cd ~/pyodide/packages/\<pkg>
- Create /pyodide/packages/\<pkg>/meta.yaml
- Set file:// and sha256 hash in meta file
- Double-check accuracy of pkg name in meta file
- python -m pyodide_build buildpkg meta.yaml
- remove old pkg wheel file from ~/pyodide/build if necessary
- cp \<pkg>/dist/\<whl file> to ~/pyodide/build
- cd to pyodide root
- PYODIDE_PACKAGES="\<pkg1>,\<pkg2>,\<pkg3>" make
- `pyodide-build serve --port 8080`
