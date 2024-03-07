#!/usr/bin/env bash

# Update package index and install nginx
sudo apt-get update
sudo apt-get -y install nginx

# Create necessary folders
sudo mkdir -p /data/web_static/releases/test /data/web_static/shared

# Create a fake HTML file
sudo echo "<html><head></head><body>Holberton School</body></html>" | sudo tee /data/web_static/releases/test/index.html > /dev/null

# Create symbolic link
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current

# Change ownership recursively
sudo chown -R ubuntu:ubuntu /data/

# Update nginx configuration
config_text="server {
    listen 80;
    listen [::]:80 default_server;

    location /hbnb_static {
        alias /data/web_static/current/;
    }
}"
echo "$config_text" | sudo tee /etc/nginx/sites-available/default > /dev/null

# Restart nginx
sudo service nginx restart

exit 0

