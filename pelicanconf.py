#!/usr/bin/env python
# -*- coding: utf-8 -*- #

AUTHOR = 'Mariska van Willigen'
SITENAME = 'Mariska van Willigen'
SITEURL = 'https://mariskavanwilligen.github.io'

LANDING_PAGE_TITLE = "Welcome to " + SITENAME

PATH = 'content'

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = 'nl'

THEME = 'theme/MinimalXY'
NEST_HEADER_IMAGES = 'sea.jpg'
DISPLAY_PAGES_ON_MENU = 'True'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

LOAD_CONTENT_CACHE = False


STATIC_PATHS = [
    'images',
    'pages',
    ]

# Blogroll
LINKS = (('Pelican', 'https://getpelican.com/'),
         ('Python.org', 'https://www.python.org/'),
         ('Jinja2', 'https://palletsprojects.com/p/jinja/'),
         ('Albert Heijn', 'https://ah.nl/'),)
# Author
AUTHOR_INTRO = u'Hello world! I’m Mariska van Willigen'
AUTHOR_DESCRIPTION = u'Hello world! I’m Mariska van Willigen. Data scientist for Albert Heijn!'
AUTHOR_AVATAR = '/images/logo_min.png'
#AUTHOR_WEB = 'http://mypersonalsite.com'

# Social
SOCIAL = (
    ('facebook', 'https://www.facebook.com/mariska.vanwilligen.5/'),
    ('github', 'https://github.com/mariskavanwilligen'),
    ('linkedin', 'https://www.linkedin.com/in/mariska-van-willigen-09b036126/'),
)

DEFAULT_PAGINATION = False
DEFAULT_CATEGORY = 'Posts'
GOOGLE_ANALYTICS = 'G-0C50D9NRQT'
#NEST_HEADER_LOGO = '/images/logo.png'
# MENUITEMS = (('About meEE', '/aboutme.html'),
#             ('Contact', '/contact.html'),
#          )
# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True