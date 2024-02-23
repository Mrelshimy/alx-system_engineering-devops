# Puppet manifest to insstall flask 2.1.0 using pip3

package { 'python3-pip':
  ensure   => installed,
}

package { 'flask':
  ensure   => '2.1.0',
  provider => 'pip3'
}
