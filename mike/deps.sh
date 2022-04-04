apt update
apt -y upgrade

apt install -y build-essential
apt install -y clang-format-6.0
apt install -y libssl-dev libyaml-dev libreadline6-dev libncurses5-dev libffi-dev libgdbm-dev libdb-dev libltdl-dev
apt install -y libgdbm6 libtool
apt install -y zlib1g-dev
apt install -y prelink cmake patch automake autoconf autotools-dev bzip2 bison ccache texinfo pkg-config patch swig xz-utils
apt install -y texinfo dejagnu gnupg2 libdbus-glib-1-2
apt install -y git
apt install -y unzip
apt install -y wget
apt install -y gfortran
apt install -y g++
apt install -y f2c
apt install -y default-jre
apt install -y nodejs

su vagrant <<'EOF'
  cd /home/vagrant
  wget https://repo.anaconda.com/miniconda/Miniconda3-py39_4.11.0-Linux-x86_64.sh
  bash Miniconda3-py39_4.11.0-Linux-x86_64.sh -b
  echo ". /home/vagrant/miniconda3/etc/profile.d/conda.sh" >> ~/.bashrc

  git clone https://github.com/pyodide/pyodide.git
EOF
