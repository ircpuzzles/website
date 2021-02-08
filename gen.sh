rm -rf /var/www/ircpuzzles.org/public/blog/
pelican -D -s /var/www/ircpuzzles.org/website/pelicanconf.py /var/www/ircpuzzles.org/website/ -o /var/www/ircpuzzles.org/public/blog/
cp -r /var/www/ircpuzzles.org/public/blog/* /var/www/ircpuzzles.org/public/ircpuzzles.github.io/
