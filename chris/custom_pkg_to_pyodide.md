# pyodide-build mkpkg <pkg name>
# cd ~/pyodide/packages/<pkg name>
# python -m pyodide_build buildpkg meta.yaml
# Remove package's wheel from pyodide/build if necessary
# cd pyodide root
# PYODIDE_PACKAGES="<pgk name>" make
# cd pyodide/packages/<pkg name>/dist
# cp <pkg name>.whatever.whl ~/pyodide/build
# start or restart pyodide server ??? (probably not)
