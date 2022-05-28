#!/bin/bash
#https://alestic.com/2010/12/ec2-user-data-output/
exec > >(tee /var/log/user-data.log|logger -t user-data -s 2>/dev/console) 2>&1
echo BEGIN
sudo apt-get update -y
sudo apt-get upgrade -y

# Install saltstack
sudo apt-get install salt-minion -y

# Set salt master location and start minion
sudo sed -i 's/#master: salt/master: 34.253.201.12/g' /etc/salt/minion
sudo salt-minion -d

# Install Docker
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
sudo add-apt-repository \
   "deb [arch=amd64] https://download.docker.com/linux/ubuntu \
   $(lsb_release -cs) \
   stable" -y   
   
sudo apt-get update -y
sudo apt-get install docker-ce -y
sudo apt install python-pip -y && sudo pip install docker-py -y
echo END