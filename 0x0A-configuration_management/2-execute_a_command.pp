# Kill a process with Puppet
exec { 'pkill':
  command => 'pkill killmenow',
}