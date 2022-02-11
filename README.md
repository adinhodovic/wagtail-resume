# Wagtail resume

![Lint](https://github.com/adinhodovic/wagtail-resume/workflows/Test/badge.svg)
![Test](https://github.com/adinhodovic/wagtail-resume/workflows/Lint/badge.svg)
[![Coverage](https://codecov.io/gh/adinhodovic/wagtail-resume/branch/main/graphs/badge.svg)](https://codecov.io/gh/adinhodovic/wagtail-resume/branch/main)
[![Supported Python versions](https://img.shields.io/pypi/pyversions/wagtail-resume.svg)](https://pypi.org/project/wagtail-resume/)
[![PyPI Version](https://img.shields.io/pypi/v/wagtail-resume.svg?style=flat)](https://pypi.org/project/wagtail-resume/)

Wagtail-resume is a reusable Wagtail page model designed to make the creation of your resume easy and quick.

Feaures:

- Easy management of your resume in Wagtail
- Search engine optimized using HTML meta tags - make it easier to find your resume in Google
- Flexible section creation of projects, blog posts, etc
- Easy customizations of font, icons and background color
- Easily reference other content on your Wagtail page as blog posts
- HTML based, no more sending of PDFs, just a url for sharing
- In-site Weasyprint button for a PDF version
- Responsive for mobile and tablet

## Preview

![Resume Preview](https://i.imgur.com/b0TxeGe.png)

The full resume example is [live and accesible here.](https://hodovi.cc/wagtail-resume-sample)

## Dependencies

- Wagtail-metadata
    - It uses wagtail-metadata for all meta & SEO fields.
- Wagtail-markdown
- Weasyprint
    - Uses Weasyprint to generate a PDF from the HTML page.

## Installation

Install wagtail-resume with pip:

`pip install wagtail-resume`

Add the application and dependencies to installed Django applications:

```py
INSTALLED_APPS = [
    ...
    "wagtailmetadata",
    "wagtailmarkdown",
    "wagtail_resume",
    ...
]
```

Add the urls for generating a pdf using Weasyprint:

```py
    path("resume/", include("wagtail_resume.urls")),
```

Run the migrations.

## Getting started

Import and extend the BaseResumePage:

```python
# home/models.py
from wagtail_resume.models import BaseResumePage


class ResumePage(BaseResumePage):
    pass
```

After adding the model you'll need to make a migration

```
python manage.py makemigrations
```

... and then apply it

```
python manage.py migrate
```

Head over to the Wagtail admin and create your resume!

Weasyprint generates PDFs using the absolute URL of a resume which consists of the hostname, port and path. Therefore don't forget to configure your site's host and path in the Wagtail admin interface which is located in settings -> sites. E.g when running the server locally the host should be localhost and the port should be 8000 (or whichever port you develop locally with).

## Default Fields

Default resume fields:

- Role
- Profile picture
- Social links
- About
- Work Experience
- Contributions (Opensource/projects)
- Writing (internal Wagtail pages or external URLs)
- Education (Degrees/Courses/Certificates)

## Customization

Wagtail-resume currently supports 4 customizations:

- Heading for a section
- Icon for a section (Fontawesome)
- Font style
- Background color
- PDF generation button visibility (public, authenticated, disabled)

The background-color should be specified in hex (e.g #FFFFFF) or [css supported colors](https://www.w3schools.com/cssref/css_colors.asp) and the font should be available on Google fonts. The fonts supported are only the ones from [Google Fonts](https://fonts.google.com/) so make sure to check what fonts are available.
