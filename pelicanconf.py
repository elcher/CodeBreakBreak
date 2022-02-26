from datetime import datetime

AUTHOR = "Longcan Huang"
SITEURL = "https://elcher.github.io/CodeBreakBreak"
SITENAME = "Code Break Break"
SITETITLE = "Code Break Break"
# SITESUBTITLE = "Web Developer"
SITEDESCRIPTION = "Thoughts and Writings"
SITELOGO = SITEURL + "/images/profile.jpg"
# FAVICON = SITEURL + "/images/favicon.ico"

BROWSER_COLOR = "#333333"
PYGMENTS_STYLE = "monokai"

ROBOTS = "index, follow"

THEME = "/home/elch/pelican-themes/Flex"


# Enable i18n plugin.
# PLUGINS = ["i18n_subsites"]
# Enable Jinja2 i18n extension used to parse translations.
# JINJA_ENVIRONMENT = {"extensions": ["jinja2.ext.i18n"]}

PATH = "content"
OUTPUT_PATH = "output/"
TIMEZONE = "America/Los_Angeles"

DISABLE_URL_HASH = True


I18N_TEMPLATES_LANG = "en"
DEFAULT_LANG = "en"
OG_LOCALE = "en_US"
LOCALE = "en_US"

DATE_FORMATS = {
    "en": "%B %d, %Y",
}

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

USE_FOLDER_AS_CATEGORY = False
MAIN_MENU = True
HOME_HIDE_TAGS = True

# Social widget
SOCIAL = (
    # ("You can add links in your config file", "#"),
    ("github", "https://github.com/elcher"),
    # ("Another social link", "#"),
)

MENUITEMS = (
    ("Archives", "/archives.html"),
    ("Categories", "/categories.html"),
    ("Tags", "/tags.html"),
)


CC_LICENSE = {
    "name": "Creative Commons Attribution-ShareAlike",
    "version": "4.0",
    "slug": "by-sa",
    "icon": True,
    "language": "en_US",
}

COPYRIGHT_YEAR = datetime.now().year
DEFAULT_PAGINATION = 10

# DISQUS_SITENAME = "flex-pelican"
# ADD_THIS_ID = "ra-55adbb025d4f7e55"

STATIC_PATHS = ["images"]

# EXTRA_PATH_METADATA = {
# "extra/custom.css": {"path": "static/custom.css"},
# }

# CUSTOM_CSS = "static/custom.css"


# Blogroll
# LINKS = (
# ("Pelican", "https://getpelican.com/"),
# ("Python.org", "https://www.python.org/"),
# ("Jinja2", "https://palletsprojects.com/p/jinja/"),
# ("You can modify those links in your config file", "#"),
# )


# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True

MARKUP = ("md", "ipynb")

from pelican_jupyter import markup as nb_markup

PLUGINS = [nb_markup]

IGNORE_FILES = [".ipynb_checkpoints"]
