# Install puppet-lint 2.1.1 version with Puppet
package { 'puppet-lint -v 2.1.1':
  ensure => 'installed',
  provider => 'gem',
}