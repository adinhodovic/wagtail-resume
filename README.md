# Wagtail resume

[![Build status](https://gitlab.com/hodovicadin/wagtail-resume/badges/master/pipeline.svg)](https://gitlab.com/hodovicadin/wagtail-resume/commits/master)
[![Coverage](https://gitlab.com/hodovicadin/wagtail-resume/badges/master/coverage.svg)](https://gitlab.com/hodovicadin/wagtail-resume/commits/master)
[![Supported Python versions](https://img.shields.io/pypi/pyversions/wagtail-resume.svg)](https://pypi.org/project/wagtail-resume/)
[![PyPI Version](https://img.shields.io/pypi/v/wagtail-resume.svg?style=flat)](https://pypi.org/project/wagtail-resume/)

Wagtail-resume is a reusable Wagtail page model designed to make the creation of a good resume easy and quick. Additionally, it will be fully integrated into your site/blog.

## Preview

![Resume Preview](https://i.imgur.com/b0TxeGe.png)

The full resume example is [live and accesible here.](https://hodovi.cc/wagtail-resume-sample)


## Dependencies

- Wagtail-metadata
    - It uses wagtail-metadata for all meta & SEO fields.

## Installation

Install wagtail-resume with pip:

`pip install wagtail-resume`

Add the application to installed Django applications:

```py
INSTALLED_APPS = [
    ...
    "wagtail_resume",
    ...
]
```

Run the migrations.

## Getting started

Import and extend the BaseResumePage:

```python
from wagtail_resume.models import BaseResumePage


class ResumePage(BaseResumePage):
    pass
```

Head over to the Wagtail admin and create your resume!

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

The background-color should be specified in hex (e.g #FFFFFF) or [css supported colors](https://www.w3schools.com/cssref/css_colors.asp) and the font should be available on Google fonts. The fonts supported are only the ones from [Google Fonts](https://fonts.google.com/) so make sure to check what fonts are available.
