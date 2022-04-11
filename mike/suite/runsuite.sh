source ~/miniconda3/etc/profile.d/conda.sh
conda create -y --name suite python=3.10
conda activate suite

cd _workspace
git clone git@github.com:terminal-labs/epython.git
vagrant up
cd epython
pip install -e .
cd ..
pip install -r requirements.txt
python client.py
cd ..

cp plugins/examples/default.py plugins/default.py

cd plugins/examples/pack
zip test.zip -D *
mv test.zip ../../test.zip
cd ../../..
