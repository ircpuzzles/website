rm -rf /var/www/ircpuzzles.org/public/blog/
pelican -D -s /var/www/ircpuzzles.org/public_src/pelican.conf.py /var/www/ircpuzzles.org/public_src/ -o /var/www/ircpuzzles.org/public/blog/
cp -r /var/www/ircpuzzles.org/public/blog/* /var/www/ircpuzzles.org/ircpuzzles.github.io/
