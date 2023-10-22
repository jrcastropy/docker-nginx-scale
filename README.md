# Run Flask in Docker with scale with HTTPS domain name using NGINX in Ubuntu 22.04

This repo is a template to run flask with docker-compose that is scalable and and uses a domain name.

## Installation

### Requirements
- docker
- docker-compose
- python
- flask
- nginx
- Ubuntu 22.04 Server
- domain

### First step if to Clone this repo to your server

### Point your domain to the server with A records
- Create 'A' record to ubuntu server's IP address with "@" as hostname
- Create 'A' record to ubuntu server's IP address with "www" as hostname

### Update Ubuntu Server
[Update Ubuntu](https://www.cyberciti.biz/faq/upgrade-update-ubuntu-using-terminal/)
```bash
sudo apt-get update
sudo apt-get upgrade
```

### Install Docker
[How to install docker in Ubuntu 22.04](https://www.digitalocean.com/community/tutorials/how-to-install-and-use-docker-on-ubuntu-22-04)
```bash
sudo apt update
sudo apt install apt-transport-https ca-certificates curl software-properties-common
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg
echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
sudo apt update
apt-cache policy docker-ce
sudo apt install docker-ce
```
### Check if docker is running
```bash
sudo systemctl status docker
```

### Install docker-compose
[Install Docker Compose on Ubuntu 22.04](https://cloudinfrastructureservices.co.uk/how-to-install-and-use-docker-compose-on-ubuntu-22-04/)
```bash
sudo apt install docker-compose
sudo chmod +x /usr/local/bin/docker-compose
```

### Check if docker-compose is running
```bash
docker compose version
```

### Install Nginx
[Install NGINX in Ubuntu 22.04](https://www.digitalocean.com/community/tutorials/how-to-install-nginx-on-ubuntu-22-04)
```bash
sudo apt update
sudo apt install nginx
sudo ufw app list
sudo ufw allow 'Nginx HTTP'
systemctl status nginx
```
## Setup

### Remove NGINX Defaults
```bash
sudo rm /etc/nginx/sites-enabled/default
sudo nano /etc/nginx/sites-enabled/<whatever you want, no spaces>
```
type the text below in the /etc/nginx/sites-enabled/<whatever you want, no spaces>
then save it
```bash
server {
        listen 80;
        server_name www.insertdomainhere.com insertdomainhere.com;
        
        location / {
                proxy_pass http://localhost:8000;
                include /etc/nginx/proxy_params;
                proxy_redirect off;
        }
}
```


### UFW Allow
```bash
sudo ufw allow http/tcp
sudo ufw allow ssh
sudo ufw allow https
sudo ufw enable
sudo ufw status
```

### Get certificates for SSL
```bash
apt-get update
sudo apt-get install certbot
apt-get install python3-certbot-nginx
nginx -t && nginx -s reload
sudo certbot --nginx -d insertdomainhere.com -d www.insertdomainhere.com
```
### SSL new folder
Create a folder inside nginx and name it ssl

### Copy SSL cert pem file and private key
Get the contenst of fullchain.pem
```bash
sudo nano /etc/letsencrypt/live/insertdomainhere.com/fullchain.pem
```
copy and save it inside ./nginx/ssl/fullchain.pem

Get the contenst of privkey.pem
```bash
sudo nano /etc/letsencrypt/live/insertdomainhere.com/privkey.pem
```
copy and save it inside ./nginx/ssl/privkey.pem

## Usage
```docker-compose
docker-compose up --build --scale web=3
```

## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

Please make sure to update tests as appropriate.

## Links
https://business-science.github.io/shiny-production-with-aws-book/https-nginx-docker-compose.html