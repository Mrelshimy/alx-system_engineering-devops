# Puppet manifest to insstall flask 2.1.0 using pip3

exec { 'install-flask':
  command => 'pip3 install flask==2.1.0 Werkzeug==2.1.1',
  path    => ['/usr/bin', '/usr/sbin'],
}
