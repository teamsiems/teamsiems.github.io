import datetime

AUTHOR = 'c'
SITENAME = 'teamsiems'
SITESUBTITLE = 'A team of Siems observing life on the web.'
SITEURL = ""

CURRENT_YEAR = datetime.datetime.now().year

PATH = "content"
OUTPUT_PATH = 'docs'

TIMEZONE = 'America/Chicago'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (
    ("Pelican", "https://getpelican.com/"),
    ("Python.org", "https://www.python.org/"),
    ("Jinja2", "https://palletsprojects.com/p/jinja/"),
    ("You can modify those links in your config file", "#"),
)

# Social widget
SOCIAL = (
    ("You can add links in your config file", "#"),
    ("Another social link", "#"),
)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

THEME = 'themes/simple'

# Enable article neighbors for next/previous navigation.
PLUGINS = [
    'neighbors',
]

MARKDOWN = {
    'extension_configs': {
        'markdown.extensions.extra': {},  # Includes attr_list
        # OR specifically:
        'markdown.extensions.attr_list': {},
    },
    'output_format': 'html5',
}
