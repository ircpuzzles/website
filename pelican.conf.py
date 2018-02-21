# -*- coding: utf-8 -*-

THEME = '/home/yano/dev/pelican-themes/fresh'
AUTHOR = u'yano'
SITENAME = u"#ircpuzzles"
SITEURL = u'https://ircpuzzles.org'

TYPOGRIFY = True

ARTICLE_URL = '{date:%Y}/{date:%m}/{slug}/'
ARTICLE_SAVE_AS = '{date:%Y}/{date:%m}/{slug}/index.html'
YEAR_ARCHIVE_SAVE_AS = '{date:%Y}/index.html'
MONTH_ARCHIVE_SAVE_AS = '{date:%Y}/{date:%m}/index.html'

GITHUB_URL = u'https://github.com/ircpuzzles/'
DISQUS_SITENAME = u'ircpuzzles'
REVERSE_CATEGORY_ORDER = True
OUTPUT_PATH = '/var/www/ircpuzzles.org/public/'
RELATIVE_URLS = True
TIMEZONE = 'UTC'

FEED_RSS = 'feeds/all.rss.xml'
CATEGORY_FEED_RSS = 'feeds/%s.rss.xml'

DEFAULT_LANG = 'en'

STATIC_PATHS = ['images',]


SOCIAL = (
    ('twitter', 'https://twitter.com/ircpuzzles'),
 )


DATE_FORMATS = {
    'en': '%Y-%m-%d %H:%M',
}
