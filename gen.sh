## delete the current version (makes sure files we get rid of are gone and not lingering around)
rm -rf /var/www/ircpuzzles.org/blog/

## generate website
/opt/ircpuzzles.org_website_venv/bin/pelican -D -s /opt/ircpuzzles.org_website/pelicanconf.py /opt/ircpuzzles.org_website/ -o /var/www/ircpuzzles.org/blog/
