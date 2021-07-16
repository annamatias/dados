#!/bin/bash

apt update -yes
amazon-linux-extras install -y lamp-mariadb10.2-php7.2
apt install -y httpd mariadb-server
systemctl start httpd
systemcl enable httpd
systemctl start mariadb
systemcl enable mariadb
usermod -a -G apache ec2-user
chown -R ecr-user:apache /var/www