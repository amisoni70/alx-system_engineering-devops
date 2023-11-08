# a typo error naming of the .php file
exec { 'renaming the apache config file':
    command => "/bin/sed -i 's/.phpp/.php/' /var/www/html/wp-settings.php",
}
