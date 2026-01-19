import re

from django import template
from markdown import markdown

register = template.Library()


@register.filter
def space_to_plus(value):
    """Replace spaces with plus signs for URL encoding (used in Google Fonts URLs)."""
    return value.replace(" ", "+")


@register.filter
def markdown_to_bullets(value):
    """Convert markdown to HTML with bullet points and links preserved for academic CV."""
    if not value:
        return ""

    # Convert markdown to HTML with autolink extension
    html = markdown(value, extensions=["extra", "nl2br"])

    # Also convert plain URLs to clickable links (regex pattern for URLs)
    url_pattern = r'(?<!href=")(?<!src=")(https?://[^\s<>"]+)'
    html = re.sub(url_pattern, r'<a href="\1">\1</a>', html)

    return html
