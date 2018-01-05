# install docker
apt-get update -y
apt-get install \
    apt-transport-https \
    ca-certificates \
    curl \
    software-properties-common
# https://github.com/moby/moby/issues/22599
curl -s https://yum.dockerproject.org/gpg | sudo apt-key add
apt-key fingerprint 58118E89F3A912897C070ADBF76221572C52609D
add-apt-repository "deb https://apt.dockerproject.org/repo ubuntu-$(lsb_release -cs) main"
apt-get update -y
apt-get install -y docker-engine=1.13.0-0~ubuntu-xenial
#curl -fsSL https://download.docker.com/apt-key fingerprint 0EBFCD88linux/ubuntu/gpg | apt-key add -
# Checking only
#apt-key fingerprint 0EBFCD88
#add-apt-repository \
#   "deb [arch=amd64] https://download.docker.com/linux/ubuntu \
#   $(lsb_release -cs) \
#   stable"
#apt-get update -y
#apt-get install docker-ce
# install docker-compose
curl -L https://github.com/docker/compose/releases/download/1.18.0/docker-compose-`uname -s`-`uname -m` -o /usr/local/bin/docker-compose
chmod +x /usr/local/bin/docker-compose
# Avoid sudo
usermod -aG docker ubuntu
