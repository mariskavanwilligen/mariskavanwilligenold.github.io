#!/usr/bin/env python
# -*- coding: utf-8 -*- #

AUTHOR = 'Mariska van Willigen'
SITENAME = 'Mariska van Willigen'
SITEURL = ''

LANDING_PAGE_TITLE = "Welcome to " + SITENAME

PATH = 'content'

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = 'nl'

THEME = 'themes/MinimalXV'
NEST_HEADER_IMAGES = 'sea.jpg'
#DISPLAY_PAGES_ON_MENU = 'True'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

STATIC_PATHS = [
    'images',
    'pages',
    ]

# Blogroll
LINKS = (('Pelican', 'https://getpelican.com/'),
         ('Python.org', 'https://www.python.org/'),
         ('Jinja2', 'https://palletsprojects.com/p/jinja/'),
         ('Albert Heijn', 'https://ah.nl/'),)

# Social widget
SOCIAL = (('My Linkedin', 'https://www.linkedin.com/in/mariska-van-willigen-09b036126/'),
          ('Join Albert Heijn', 'https://werk.ah.nl/'),)

DEFAULT_PAGINATION = False
DEFAULT_CATEGORY = 'somethingelse'
#NEST_HEADER_LOGO = '/images/logo.png'
MENUITEMS = (('About me', '/aboutme.html'),
            ('Contact', '/contact.html'),
         )
# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True