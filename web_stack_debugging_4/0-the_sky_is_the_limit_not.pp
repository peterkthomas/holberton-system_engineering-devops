# Increase the default ulimit
exec { 'fix nginx ulimit':
  command => 'sed -i "s/15/$( ulimit -n )/" /etc/default/nginx',
  path    => '/usr/local/bin/:/bin/'
} ->

# next restart nginx
exec { 'restart nginx':
  command => 'service nginx restart',
  path    => '/usr/bin/'
}
