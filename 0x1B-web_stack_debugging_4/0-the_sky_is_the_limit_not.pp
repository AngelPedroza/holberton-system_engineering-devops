exec { '/bin/bash':
  command => 'sed -i "s/worker_processes.*/worker_processes 10;/" /etc/nginx/nginx.conf',
  path    => ['/usr/bin', '/usr/sbin'],
}

service { 'nginx':
  ensure  => running,
  restart => 'sudo service nginx restart',
}