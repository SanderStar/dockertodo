Docker todo app
===============

Build with mongo, nginx, node and python

Database: mongo

Reverse proxy: nginx

Frontend
- node and html
- python and html

Requirements:
- vagrant

Steps for running
=================

@host system
Install vagrant in your environment

@vm system
vagrant up

vagrant ssh

sudo /vagrant

sudo docker-compose build
sudo docker-compose up

@host system
See Vagrantfile for host ip address: 192.168.10.10
See docker-compose.yml for port mapping 8080 to 8080 for nginx
Start browser session http://192.168.10.10:8080
