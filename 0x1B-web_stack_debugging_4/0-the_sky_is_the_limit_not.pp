# Add more workers
exec { '/bin/bash':
  command => 'sed -i "s/worker_processes.*/worker_processes 10;/" /etc/nginx/nginx.conf ; sudo service nginx restart',
  path    => ['/usr/bin', '/bin'],
}