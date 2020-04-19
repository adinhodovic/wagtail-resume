import os

from django.utils.translation import ugettext_lazy as _

DEBUG = True

SECRET_KEY = "very-secret"

ROOT_URLCONF = "tests.urls"

DATABASES = {"default": {"ENGINE": "django.db.backends.sqlite3", "NAME": "db.sqlite3"}}

DJANGO_APPS = [
    "django.contrib.auth",
    "django.contrib.contenttypes",
]

MIDDLEWARE = [
    "wagtail.core.middleware.SiteMiddleware",
    "django.middleware.locale.LocaleMiddleware",
]

THIRD_PARTY_APPS = [
    "wagtail.contrib.forms",
    "wagtail.contrib.redirects",
    "wagtail.embeds",
    "wagtail.sites",
    "wagtail.users",
    "wagtail.snippets",
    "wagtail.documents",
    "wagtail.images",
    "wagtail.search",
    "wagtail.admin",
    "wagtail.core",
    "wagtailmarkdown",
    "wagtailmetadata",
    "modelcluster",
    "taggit",
]

LOCAL_APPS = ["wagtail_resume", "tests"]

INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
            ]
        },
    }
]

LOCALE_PATHS = [
    os.path.join(os.path.dirname(__file__), "locale"),
]
LANGUAGES = (
    ("en-us", _("English")),
    ("sv", _("Swedish")),
)

SITE_ID = 1

WAGTAIL_SITE_NAME = "My Example Site"
