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
        title="Resume",
        full_name="Adin Hodovic",
        role="Software engineer",
        pdf_generation_visibility="always",
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
        title="Resume",
        full_name="Adin Hodovic",
        role="Software engineer",
        font="lato",
        pdf_generation_visibility="always",
    )
    site.root_page.add_child(instance=resume)
    # Test random page pdf generation
    url = f"{reverse('generate_resume_pdf')}?page_id={resume.id}"
    res = client.get(url)
    assert "adin-hodovic" in res["content-disposition"]
    assert res.status_code == 200
    assert res["content-type"] == "application/pdf"


def test_weasyprint_unauthenticated(client, mocker):
    mocker.patch("wagtail_resume.views.HTML")
    site = Site.objects.first()
    resume = CustomResumePage(
        title="Resume",
        full_name="Adin Hodovic",
        role="Software engineer",
        font="lato",
        pdf_generation_visibility="authenticated",
    )
    site.root_page.add_child(instance=resume)
    # Test random page pdf generation
    url = f"{reverse('generate_resume_pdf')}?page_id={resume.id}"
    res = client.get(url)
    assert b"You need to be authenticated to generate a resume PDF file." in res.content
    assert res.status_code == 403


def test_weasyprint_disabled(client, mocker):
    mocker.patch("wagtail_resume.views.HTML")
    site = Site.objects.first()
    resume = CustomResumePage(
        title="Resume",
        full_name="Adin Hodovic",
        role="Software engineer",
        font="lato",
        pdf_generation_visibility="never",
    )
    site.root_page.add_child(instance=resume)
    # Test random page pdf generation
    url = f"{reverse('generate_resume_pdf')}?page_id={resume.id}"
    res = client.get(url)
    assert b"<h1>PDF generation is disabled for this resume.</h1>" in res.content
    assert res.status_code == 400


def test_weasyprint_with_no_page_id(client, mocker):
    mocker.patch("wagtail_resume.views.HTML")
    site = Site.objects.first()
    resume = CustomResumePage(
        title="Resume",
        full_name="Adin Hodovic",
        role="Software engineer",
        font="lato",
    )
    site.root_page.add_child(instance=resume)
    # Test random page pdf generation
    url = f"{reverse('generate_resume_pdf')}"
    res = client.get(url)
    assert b"Missing page id for resume generation" in res.content
    assert res.status_code == 400


def test_weasyprint_with_no_number(client, mocker):
    mocker.patch("wagtail_resume.views.HTML")
    site = Site.objects.first()
    resume = CustomResumePage(
        title="Resume",
        full_name="Adin Hodovic",
        role="Software engineer",
        font="lato",
    )
    site.root_page.add_child(instance=resume)
    # Test random page pdf generation
    url = f"{reverse('generate_resume_pdf')}?page_id={resume.id}'"
    res = client.get(url)
    assert b"Page id is not a number" in res.content
    assert res.status_code == 400


def test_weasyprint_no_resume(client, mocker):
    mocker.patch("wagtail_resume.views.HTML")
    site = Site.objects.first()
    resume = CustomResumePage(
        title="Resume",
        full_name="Adin Hodovic",
        role="Software engineer",
        font="lato",
    )
    site.root_page.add_child(instance=resume)
    # Test non existent resume
    url = f"{reverse('generate_resume_pdf')}?page_id=9999"
    res = client.get(url)
    assert res.status_code == 404


def test_weasyprint_logger_warnings_disabled():
    logger = logging.getLogger("weasyprint")
    assert logger.level == 40
