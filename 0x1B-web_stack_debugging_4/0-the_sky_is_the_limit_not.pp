exec { '/bin/bash':
  command => 'sed -i "s/worker_processes.*/worker_processes 11;/" /etc/nginx/nginx.conf',
  creates => '/var/www/html/wp-includes/class-wp-locale.phpp',
  path    => ['/usr/bin', '/usr/sbin'],
}

service { 'nginx':
  ensure  => running,
  restart => 'sudo service nginx restart',
}