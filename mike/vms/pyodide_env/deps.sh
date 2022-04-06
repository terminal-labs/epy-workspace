mkdir /vagrant/temp

if [ ! -f "/vagrant/temp/deps" ]; then
  apt update
  apt -y upgrade

  apt install -y build-essential
  apt install -y linux-headers-$(uname -r)
  apt install -y libgdbm6 libdbus-glib-1-2 libtool
  apt install -y libssl-dev libyaml-dev libreadline6-dev libncurses5-dev libffi-dev libgdbm-dev libdb-dev libltdl-dev
  apt install -y zlib1g-dev
  apt install -y clang-format-6.0
  apt install -y prelink cmake patch automake autoconf bzip2 bison ccache pkg-config swig xz-utils autotools-dev
  apt install -y texinfo dejagnu gnupg2
  apt install -y git
  apt install -y unzip
  apt install -y wget
  apt install -y gfortran
  apt install -y g++
  apt install -y f2c
  apt install -y default-jre
  apt install -y nodejs
  apt install -y npm
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
  if [ ! -f "/vagrant/temp/clone" ]; then
    git clone https://github.com/pyodide/pyodide.git
    touch /vagrant/temp/clone
  fi
  cd pyodide
  git checkout 0.20.0a1

  if [ ! -f "/vagrant/temp/patch" ]; then
    patch cpython/Makefile < /vagrant/patch00
    touch /vagrant/temp/patch
  fi

  source pyodide_env.sh

  if [ ! -f "/vagrant/temp/reqs" ]; then
    pip install -r requirements.txt
    touch /vagrant/temp/reqs
  fi

  if [ ! -f "/vagrant/temp/make" ]; then
    make
    touch /vagrant/temp/make
  fi

  cd /vagrant
  if [ ! -f "/vagrant/temp/superbuildinstalled" ]; then
    pip install -e superbuild
    touch /vagrant/temp/superbuildinstalled
  fi
  superbuild
EOF
