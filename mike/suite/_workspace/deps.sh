mkdir /vagrant/temp

if [ ! -f "/vagrant/temp/deps" ]; then
  apt update
  apt -y upgrade

  apt install -y build-essential
  apt install -y linux-headers-$(uname -r)
  touch /vagrant/temp/deps
fi

su vagrant <<'EOF'
  cd /home/vagrant
  if [ ! -f "/vagrant/temp/conda" ]; then
    wget https://repo.anaconda.com/miniconda/Miniconda3-py39_4.11.0-Linux-x86_64.sh
    bash Miniconda3-py39_4.11.0-Linux-x86_64.sh -b
    echo ". /home/vagrant/miniconda3/etc/profile.d/conda.sh" >> ~/.bashrc
    touch /vagrant/temp/conda
  fi
  source /home/vagrant/miniconda3/etc/profile.d/conda.sh
  source .bashrc

  if [ ! -f "/vagrant/temp/condaenv" ]; then
    conda create -y --name epy python=3.10
    touch /vagrant/temp/condaenv
  fi
  conda activate epy
  cd /vagrant/backendserver
  pip install -r requirements.txt
  nohup python server.py > log.txt 2>&1 &
EOF
