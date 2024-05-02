# Puppet Manifest to  install flask from pip3.

package { 'python3-pip':
  ensure => installed,
}

package { 'flask':
  ensure   => '2.1.0',   # Specify the desired version of Flask.
  provider => 'pip3',    # Use pip3 as the package provider.
  require  => Package['python3-pip'], # Ensure pip3 is installed before installing Flask.
}
