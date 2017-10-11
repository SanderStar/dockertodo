# -*- mode: ruby -*-
# vi: set ft=ruby :
Vagrant.configure(2) do |config|
  config.vm.box = "ubuntu/xenial64"
  config.vm.network "private_network", ip: "192.168.10.10"

  config.vm.provider "virtualbox" do |vbox|
    vbox.memory = 1024
    vbox.cpus = 2
    vbox.customize ["modifyvm", :id, "--ioapic", "on"]
  end

end
