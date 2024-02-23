# Puppet Manifest to install flask from pip3.

package { 'flask':
  ensure   => '2.1.0',  # Required version
  provider => 'pip3',   # pip3 as provider
}
