#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Belfast Science Cafe'
SITENAME = u'Belfast Science Cafe'
SITEURL = ''
TIMEZONE = 'Europe/London'


DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# Blogroll
LINKS =  (('What should we link to?', 'http://getpelican.com/'),
          ('Python.org', 'http://python.org/'),
          ('Jinja2', 'http://jinja.pocoo.org/'))

# Social widget
SOCIAL = (('Facebook', '#'),
          ('Twitter?', '#'),)

DEFAULT_PAGINATION = 5

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

THEME = 'themes/notmyidea'
DISPLAY_CATEGORIES_ON_MENU = False
INDEX_SAVE_AS = 'pages/blog.html'
PLUGIN_PATH = '../pelican-plugins'
PLUGINS = ['liquid_tags.img']
