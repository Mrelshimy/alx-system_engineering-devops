# Fix 500 error for GET HTTP method

exec {'strace':
  provider => shell,
  command  => 'sed -i "s/phpp/php/g" /var/www/html/wp-settings.php'
}
