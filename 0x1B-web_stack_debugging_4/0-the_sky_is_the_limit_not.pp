# Increase server accepted requests rate

exec { 'IncreaseLimit':
  command => 'sed -i "s/15/4096/" /etc/default/nginx',
  path    => '/usr/local/bin/:/bin/'
}

-> exec { 'restartNginx':
  command => 'nginx restart',
  path    => '/etc/init.d/'
}
