# Puppet manifest to execute a command pkill to killmenow
exec { 'kill__killmenow':
  command  => '/usr/bin/pkill  killmenow',
}
