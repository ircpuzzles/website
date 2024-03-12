# -*- coding: utf-8 -*-

#PLUGIN_PATHS = ['/home/yano/dev/pelican-plugins/']
THEME = '/opt/ircpuzzles.org_themes/eevee/'
#THEMEPATH = '/home/yano/dev/pelican-themes'
#THEME = 'eevee'
AUTHOR = u'yano'
SITENAME = u"#ircpuzzles"
SITEURL = 'https://blog.ircpuzzles.org/'
DOMAIN_PLAUSIBLE = 'blog.ircpuzzles.org'

TYPOGRIFY = False

ARTICLE_URL = '{date:%Y}/{date:%m}/{slug}/'
ARTICLE_SAVE_AS = '{date:%Y}/{date:%m}/{slug}/index.html'

AUTHOR_URL = 'author/{slug}/'
AUTHOR_SAVE_AS = 'author/{slug}/index.html'
AUTHORS_URL = 'authors/'
AUTHORS_SAVE_AS = 'authors/index.html'

TAG_URL = 'tag/{slug}/'
TAG_SAVE_AS = 'tag/{slug}/index.html'
TAGS_URL = 'tags/'
TAGS_SAVE_AS = 'tags/index.html'

YEAR_ARCHIVE_SAVE_AS = '{date:%Y}/index.html'
MONTH_ARCHIVE_SAVE_AS = '{date:%Y}/{date:%m}/index.html'

GITHUB_URL = 'https://github.com/ircpuzzles/'

# Disabled Disqus comments
#DISQUS_SITENAME = 'ircpuzzles'
COMMENTS_ON_PAGES = False


REVERSE_CATEGORY_ORDER = True
PATH = 'content'
RELATIVE_URLS = False
TIMEZONE = 'UTC'

FEED_RSS = 'feeds/all.rss.xml'
CATEGORY_FEED_RSS = 'feeds/%s.rss.xml'

DEFAULT_LANG = 'en'

STATIC_PATHS = ['images', 'static']


SOCIAL = (
    ('<i class="fa fa-twitter" aria-hidden="true"></i> Twitter', 'https://twitter.com/ircpuzzles'),
    ('<i class="fa fa-github" aria-hidden="true"></i> Github', 'https://github.com/ircpuzzles'),
    ('<i class="fa fa-twitter" aria-hidden="true"></i> Mastodon', 'https://fosstodon.org/@ircpuzzles'),
 )


DATE_FORMATS = {
    'en': '%Y-%m-%d %H:%M',
}

DISPLAY_PAGES_ON_MENU = True
DISPLAY_CATEGORIES_ON_MENU = True


CATEGORY_URL = 'category/{slug}/'
CATEGORY_SAVE_AS = 'category/{slug}/index.html'
CATEGORIES_URL = 'categories/'
CATEGORIES_SAVE_AS = 'categories/index.html'

DIRECT_TEMPLATES = ['index', 'categories', 'archives', 'search']

PLUGIN_PATHS = ['/opt/ircpuzzles.org_plugins/']
PLUGINS = ['assets', 'extract_toc', 'headerid', 'lightbox', 'neighbors', 'related_posts', 'series', 'tipue_search']


USE_AUTHOR_CARD = False

#THEME_PRIMARY = 'pink'
#THEME_ACCENT = 'pink'

LINKS = (
    ('Libera.Chat', 'https://libera.chat/'),
)


USE_TWITTER_CARDS = True
TWITTER_USERNAME = 'ircpuzzles'
USE_OPEN_GRAPH = True

#TYPOGRIFY_IGNORE_TAGS = ['pre', 'code', 'meta', 'title']

META_FOOTER = False
