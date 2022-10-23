from datetime import datetime

AUTHOR = "Deson Alleyne"
#    When developing locally, you may want to set the following variable: SITEURL = http://localhost:8000
SITEURL = "http://localhost:8000"
SITENAME = "Deson Alleyne"
SITETITLE = "Deson Alleyne"
SITESUBTITLE = "Software Developer | CNC Enthusiast | Tinkerer"
SITEDESCRIPTION = "Just sharing my adventures..."
SITELOGO = '/images/avatar.jpg'
# FAVICON = '/images/favicon.ico'

#USER_LOGO_URL = '/images/avatar.jpg' 
#USER_FAVICON_URL = 'images/avatar.jpg'
BROWSER_COLOR = "#333333"
BROWSER_COLOR = "#f00"

ROBOTS = "index, follow"

PATH = "content"
OUTPUT_PATH = "docs/"

TIMEZONE = "America/Guyana"
DEFAULT_LANG = 'en'

I18N_TEMPLATES_LANG = "en"
#OG_LOCALE = "en_US"
#LOCALE = "en_US"

DATE_FORMATS = {
    "en": "%B %d, %Y",
}

DISABLE_URL_HASH = True

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = "feeds/all.atom.xml"
CATEGORY_FEED_ATOM = "feeds/{slug}.atom.xml"
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None


USE_FOLDER_AS_CATEGORY = True
MAIN_MENU = True
HOME_HIDE_TAGS = True
LINKS_IN_NEW_TAB = 'external' 
DEFAULT_PAGINATION = 10

MENUITEMS = (
    ("Archives", "/archives.html"),
    ("Categories", "/categories.html"),
    ("Tags", "/tags.html"),
)

xMENUITEMS = (('about', '/pages/about.html'),
             ('projects', '/pages/projects.html'),
             ('archives', '/pages/archives.html')
             )


# Blogroll
LINKS = (('resume', '/resume'),
         )
         

# Social widget

SOCIAL = (('linkedin', 'https://www.linkedin.com/in/desonalleyne'),
          ('github', 'https://github.com/desonalleyne'),
          )



# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True


#THEME = '/home/deson/pelican-themes/zurb-F5-basic'
#THEME = '/home/deson/pelican-themes/twenty-html5up'
#THEME = '/home/deson/pelican-themes/taman'
#THEME = '/home/deson/pelican-themes/svbhack'
#THEME = '/home/deson/pelican-themes/pelican-cait'
#THEME = '/home/deson/pelican-themes/pelican-blue'
#THEME = '/home/deson/pelican-themes/hyde'

THEME = '/home/deson/pelican-themes/Flex'
THEME_COLOR = 'light'
THEME_COLOR_AUTO_DETECT_BROWSER_PREFERENCE = False
THEME_COLOR_ENABLE_USER_OVERRIDE = True

PYGMENTS_STYLE = "monokai"
PYGMENTS_STYLE_DARK = 'monokai'
PYGMENTS_STYLE = 'emacs'

#

## Flex theme config

# Whether to open LINKS in a new window or not. If unset, True, None or all then 
# all LINKS will open in a new window. If external only LINKS to external websites 
# will open in a new window, internal links will open in the same window. With any 
# other value (recommended False) all links will open in the same window.

# PLUGIN_PATHS = ['pelican-plugins']

# PLUGINS = ['i18n_subsites']

# JINJA_ENVIRONMENT = {'extensions': ['jinja2.ext.i18n']}

#GITHUB_CORNER_URL = "https://github.com/desonalleyne"

CC_LICENSE = {
    "name": "Creative Commons Attribution-ShareAlike 4.0 International License",
    "version": "4.0",
    "slug": "by-sa",
    "icon": True,
    "language": "en_US",
}

COPYRIGHT_YEAR = datetime.now().year

DISQUS_SITENAME = "deson-alleyne-1"
ADD_THIS_ID = "ra-55adbb025d4f7e55"

STATIC_PATHS = ["images", "extra/ads.txt", "extra/CNAME"]

EXTRA_PATH_METADATA = {
    "extra/ads.txt": {"path": "ads.txt"},
    "extra/CNAME": {"path": "CNAME"},
}

USE_LESS = True
