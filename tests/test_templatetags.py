from wagtail_resume.templatetags.wagtail_resume_extras import space_to_plus


def test_space_to_plus():
    font = space_to_plus("Open Sans")
    font_url = (
        f"https://fonts.googleapis.com/css?family={font}|Roboto+Condensed&display=swap"
    )

    assert (
        font_url
        == "https://fonts.googleapis.com/css?family=Open+Sans|Roboto+Condensed&display=swap"  # pylint: disable=line-too-long
    )
