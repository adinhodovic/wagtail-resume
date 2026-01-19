from django import template
from django.utils.html import escape
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

    # Escape raw HTML so pasted <a> tags don’t survive and break output
    value = escape(value)

    return markdown(
        value,
        extensions=["extra", "nl2br", "pymdownx.magiclink"],
        output_format="html5",
    )
