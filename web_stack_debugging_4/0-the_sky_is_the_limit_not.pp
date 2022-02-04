# Increase the default ulimit
exec { 'fix nginx ulimit':
  command => 'sed -i "s/15/$( ulimit -n )/" /etc/default/nginx',
  path    => '/usr/local/bin/:/bin/'
}
