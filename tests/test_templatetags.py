from wagtail_resume.templatetags.wagtail_resume_extras import (
    markdown_to_bullets,
    space_to_plus,
)


def test_space_to_plus():
    font = space_to_plus("Open Sans")
    font_url = (
        f"https://fonts.googleapis.com/css?family={font}|Roboto+Condensed&display=swap"
    )

    assert (
        font_url
        == "https://fonts.googleapis.com/css?family=Open+Sans|Roboto+Condensed&display=swap"  # pylint: disable=line-too-long
    )


def test_markdown_to_bullets_empty():
    """Test markdown_to_bullets with empty/None input."""
    assert markdown_to_bullets("") == ""
    assert markdown_to_bullets(None) == ""


def test_markdown_to_bullets_basic():
    """Test markdown_to_bullets with basic markdown."""
    markdown_text = "- Item 1\n- Item 2\n- Item 3"
    result = markdown_to_bullets(markdown_text)
    assert "<ul>" in result
    assert "<li>Item 1</li>" in result
    assert "<li>Item 2</li>" in result
    assert "<li>Item 3</li>" in result


def test_markdown_to_bullets_with_links():
    """Test markdown_to_bullets preserves markdown links."""
    markdown_text = "Check out [Google](https://google.com) for more info"
    result = markdown_to_bullets(markdown_text)
    assert '<a href="https://google.com">Google</a>' in result


def test_markdown_to_bullets_with_plain_urls():
    """Test markdown_to_bullets converts plain URLs to clickable links."""
    markdown_text = "Visit https://example.com for details"
    result = markdown_to_bullets(markdown_text)
    assert '<a href="https://example.com">https://example.com</a>' in result


def test_markdown_to_bullets_with_bold_italic():
    """Test markdown_to_bullets handles bold and italic text."""
    markdown_text = "This is **bold** and this is *italic*"
    result = markdown_to_bullets(markdown_text)
    assert "<strong>bold</strong>" in result
    assert "<em>italic</em>" in result


def test_markdown_to_bullets_newlines():
    """Test markdown_to_bullets preserves line breaks."""
    markdown_text = "Line 1\nLine 2\nLine 3"
    result = markdown_to_bullets(markdown_text)
    assert "<br>" in result
