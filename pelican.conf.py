# -*- coding: utf-8 -*-

THEME = './themes/bootstrap2'
SITENAME = u'IRC Puzzles'
SITEURL = u'https://ircpuzzles.github.io/'

ARTICLE_URL = '{date:%Y}/{date:%m}/{date:%d}/{slug}/'
ARTICLE_SAVE_AS = '{date:%Y}/{date:%m}/{date:%d}/{slug}/index.html'
YEAR_ARCHIVE_SAVE_AS = '{date:%Y}/index.html'
MONTH_ARCHIVE_SAVE_AS = '{date:%Y}/{date:%m}/index.html'
DAY_ARCHIVE_SAVE_AS = '{date:%Y}/{date:%m}/{date:%d}/index.html'


GITHUB_URL = u'https://github.com/ircpuzzles/'
REVERSE_CATEGORY_ORDER = True
RELATIVE_URLS = True
TIMEZONE = 'UTC'

PATH = './content'


FEED_RSS = 'feeds/all.rss.xml'
CATEGORY_FEED_RSS = 'feeds/%s.rss.xml'

DEFAULT_LANG = 'en'

STATIC_PATHS = ['images',]

DATE_FORMATS = {
    'en': '%Y-%m-%d %H:%M',
}
