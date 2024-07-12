#!/usr/bin/env bash
# Sets up web servers for the deployment of web_static

# Update and upgrade the system packages
sudo apt-get -y update
sudo apt-get -y upgrade

# Check if Nginx is installed, install if not
sudo apt-get -y install nginx

# Create directories for the web_static deployment
sudo mkdir -p /data/web_static/releases/test /data/web_static/shared

# Create a test index.html file
echo "This is a test" | sudo tee /data/web_static/releases/test/index.html

# Create a symbolic link to the test directory, overwrite if it exists
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current

# Change ownership of the /data/ directory to the ubuntu user
sudo chown -hR ubuntu:ubuntu /data/

# Configure Nginx to serve the content
sudo sed -i '38i\\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}\n' /etc/nginx/sites-available/default

# Reload Nginx to apply the configuration changes
sudo service nginx start
