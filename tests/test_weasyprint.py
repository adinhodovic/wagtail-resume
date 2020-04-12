import logging

import pytest
from django.urls import reverse

pytestmark = pytest.mark.django_db


def test_weasyprint(client):
    # Test random page pdf generation
    url = "%s?resume_url=https://google.com/&name=john-doe" % reverse(
        "generate_resume_pdf"
    )
    res = client.get(url)
    assert "john-doe-resume" in res["content-disposition"]
    assert res.status_code == 200
    assert res["content-type"] == "application/pdf"


def test_weasyprint_with_font(client):
    # Test random page pdf generation
    url = "%s?resume_url=https://google.com/&name=john-doe&font=Lato" % reverse(
        "generate_resume_pdf"
    )
    res = client.get(url)
    assert "john-doe-resume" in res["content-disposition"]
    assert res.status_code == 200
    assert res["content-type"] == "application/pdf"


def test_weasyprint_logger_warnings_disabled():
    logger = logging.getLogger("weasyprint")
    assert logger.level == 40
