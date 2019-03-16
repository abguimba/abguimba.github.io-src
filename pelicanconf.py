# custom page generated with a jinja2
#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Abraham Guimbao'
SITENAME = u'abguimba'
SITEURL = 'https://abguimba.github.io'

THEME = 'themes/chunk'
OUTPUT_PATH = 'output'
PATH = 'content'

#GITHUB_URL = 'https://github.com/abguimba'
#MENUITEMS = True

## Settings used by this theme (All Optional)
DEFAULT_DATE_FORMAT = ('%d %b %Y')
SITESUBTITLE = 'Portfolio'
FOOTER_TEXT = 'Website powered by Pelican. Theme is a modified version of Chunk by onlyhavecans'
DISPLAY_PAGES_ON_MENU = True
DISPLAY_CATEGORIES_ON_MENU = False
SINGLE_AUTHOR = True
MINT = False


TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

MENUITEMS = (('Github', 'https://github.com/abguimba'),
         ('Linkedin', 'https://www.linkedin.com/in/abraham-guimbao-parra'),
         ('Twitter', 'https://www.twitter.com/abguimba'),
         ('CV', 'https://abguimba.github.io/CV.pdf'))

# Blogroll
LINKS =  (('42', 'https://42.fr/'),
         ('CV', 'https://abguimba.github.io/CV.pdf'),
         ('Github', 'https://github.com/abguimba'),
         ('Linkedin', 'https://www.linkedin.com/in/abraham-guimbao-parra'),
         ('Stack-Overflow', 'https://stackoverflow.com/users/10463714/abraham-guimbao?tab=profile'),
         ('CodeWars', 'https://www.codewars.com/users/abguimba'),
         ('Twitter', 'https://www.twitter.com/abguimba'),
         ('Home', 'https://abguimba.github.io'))

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = False

STATIC_PATHS = [
#    'images',
    'extra',
    'extra/CV.pdf',
    'extra/README.md',
    'extra/robots.txt',
    'extra/favicon.ico',
]
EXTRA_PATH_METADATA = {
#   'extra/custom.css': {'path': 'custom.css'},
    'extra/CV.pdf': {'path': 'CV.pdf'},
    'extra/README.md': {'path': 'README.md'},
    'extra/robots.txt': {'path': 'robots.txt'},
    'extra/favicon.ico': {'path': 'favicon.ico'},  # and this
#    'extra/CNAME': {'path': 'CNAME'},
#    'extra/LICENSE': {'path': 'LICENSE'},
#    'extra/README': {'path': 'README'},
}

TYPOGRIFY = True

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True
