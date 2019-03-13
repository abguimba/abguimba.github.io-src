#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

# This file is only used if you use `make publish` or
# explicitly specify it as your config file.

import os
import sys
sys.path.append(os.curdir)
from pelicanconf import *

SITEURL = 'http://abguimba.github.io'
GITHUB_URL = 'https://github.com/abguimba'
AUTHOR = u'Abraham Guimbao'
RELATIVE_URLS = False

FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = 'feeds/%s.atom.xml'

DELETE_OUTPUT_DIRECTORY = False

# Following items are often useful when publishing

#DISQUS_SITENAME = ""
#GOOGLE_ANALYTICS = ""



THEME = 'themes/chunk'
OUTPUT_PATH = 'output'
PATH = 'content'

#MENUITEMS = True

## Settings used by this theme (All Optional)
DEFAULT_DATE_FORMAT = ('%d %b %Y')
SITESUBTITLE = 'Portfolio'
FOOTER_TEXT = ' '
DISPLAY_CATEGORIES_ON_MENU = True
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

# Blogroll
LINKS = (('Github', 'https://github.com/abguimba'),
         ('Linkedin', 'https://www.linkedin.com/in/abraham-guimbao-parra/'),
         ('Twitter', 'https://www.twitter.com/abguimba'))

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = False

STATIC_PATHS = [
#    'images',
    'extra',
    'extra/robots.txt',
    'extra/favicon.ico',
]
EXTRA_PATH_METADATA = {
#   'extra/custom.css': {'path': 'custom.css'},
    'extra/robots.txt': {'path': 'robots.txt'},
    'extra/favicon.ico': {'path': 'favicon.ico'},  # and this
#    'extra/CNAME': {'path': 'CNAME'},
#    'extra/LICENSE': {'path': 'LICENSE'},
#    'extra/README': {'path': 'README'},
}


TYPOGRIFY = True

