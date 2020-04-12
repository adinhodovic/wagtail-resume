import logging

import pytest
from django.urls import reverse
from wagtail.core.models import Site

from .models import CustomResumePage

pytestmark = pytest.mark.django_db


def test_weasyprint(client, mocker):
    mocker.patch("wagtail_resume.views.HTML")

    site = Site.objects.first()
    resume = CustomResumePage(
        title="Resume", full_name="Adin Hodovic", role="Software engineer",
    )
    site.root_page.add_child(instance=resume)
    # Test random page pdf generation
    url = f"{reverse('generate_resume_pdf')}?page_id={resume.id}"
    res = client.get(url)
    assert "adin-hodovic" in res["content-disposition"]
    assert res.status_code == 200
    assert res["content-type"] == "application/pdf"


def test_weasyprint_with_font(client, mocker):
    mocker.patch("wagtail_resume.views.HTML")
    site = Site.objects.first()
    resume = CustomResumePage(
        title="Resume", full_name="Adin Hodovic", role="Software engineer", font="lato"
    )
    site.root_page.add_child(instance=resume)
    # Test random page pdf generation
    url = f"{reverse('generate_resume_pdf')}?page_id={resume.id}"
    res = client.get(url)
    assert "adin-hodovic" in res["content-disposition"]
    assert res.status_code == 200
    assert res["content-type"] == "application/pdf"


def test_weasyprint_logger_warnings_disabled():
    logger = logging.getLogger("weasyprint")
    assert logger.level == 40
