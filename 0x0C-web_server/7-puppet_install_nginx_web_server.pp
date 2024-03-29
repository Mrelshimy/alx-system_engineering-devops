# Install nginx using puppet
exec {'install_Nginx':
  command  => 'sudo apt-get update ; sudo apt-get -y install nginx',
  provider => shell,

}
exec {'Hello_World':
  command  => 'echo "Hello World!" | sudo tee /var/www/html/index.html',
  provider => shell,
}
exec {'sudo sed -i "s/listen 80 default_server;/listen 80 default_server;\\n\\tlocation \/redirect_me {\\n\\t\\treturn 301 https:\/\/blog.ehoneahobed.com\/;\\n\\t}/" /etc/nginx/sites-available/default':
  provider => shell,
}
exec {'run_Nginx':
  command  => 'sudo service nginx restart',
  provider => shell,
}
