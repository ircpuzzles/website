rm -rf /var/www/ircpuzzles.org/public/blog/
pelican -D -s /var/www/ircpuzzles.org/website/pelican.conf.py /var/www/ircpuzzles.org/website/ -o /var/www/ircpuzzles.org/public/blog/
cp -r /var/www/ircpuzzles.org/public/blog/* /var/www/ircpuzzles.org/ircpuzzles.github.io/
