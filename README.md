# Wagtail resume

Wagtail-resume is a reusable Wagtail page model designed to make creating a resume easy, fast and fully integrated into your site.

Install wagtail-resume with pip:

`pip install wagtail-resume`

Add the application to installed django applications:

```py
DJANGO_APPS = [
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
    template = "wagtail_resume/resume_page.html"
```

Head over to the Wagtail admin and creating your resume!

## Customization

Wagtail-resume currently supports two customizations: font & background-color. The background-color should be specified in hex (e.g #FFFFFF) and the font should be available on Google fonts. The fonts are only taken from [Google Fonts](https://fonts.google.com/) so make sure to check what fonts are available.
