# Increase server accepted requests rate

exec {'increaseLimit':
  provider => shell,
  command  => 'sudo sed -i "s/ULIMIT=\"-n 15\"/ULIMIT=\"-n 4096\"/" /etc/default/nginx',
  before   => Exec['restart'],
}

exec {'nginxRestart':
  provider => shell,
  command  => 'sudo service nginx restart',
}
