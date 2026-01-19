import logging

import pytest
from django.urls import reverse

from wagtail_resume.views import academic_resume_pdf, resume_pdf

pytestmark = pytest.mark.django_db


def test_weasyprint(site, resume, client, mocker):
    mocker.patch("wagtail_resume.views.HTML")

    resume.pdf_generation_visibility = "always"

    site.root_page.add_child(instance=resume)
    # Test random page pdf generation
    url = f"{reverse('generate_resume_pdf')}?page_id={resume.id}"
    res = client.get(url)
    assert "adin-hodovic" in res["content-disposition"]
    assert res.status_code == 200
    assert res["content-type"] == "application/pdf"


def test_weasyprint_with_font(site, resume, client, mocker):
    mocker.patch("wagtail_resume.views.HTML")
    resume.pdf_generation_visibility = "always"

    site.root_page.add_child(instance=resume)
    # Test random page pdf generation
    url = f"{reverse('generate_resume_pdf')}?page_id={resume.id}"
    res = client.get(url)
    assert "adin-hodovic" in res["content-disposition"]
    assert res.status_code == 200
    assert res["content-type"] == "application/pdf"


def test_weasyprint_unauthenticated(resume, site, client, mocker):
    mocker.patch("wagtail_resume.views.HTML")
    resume.pdf_generation_visibility = "authenticated"
    site.root_page.add_child(instance=resume)
    # Test random page pdf generation
    url = f"{reverse('generate_resume_pdf')}?page_id={resume.id}"
    res = client.get(url)
    assert b"You need to be authenticated to generate a resume PDF file." in res.content
    assert res.status_code == 403


def test_weasyprint_authenticated(site, resume, rf, django_user_model, mocker):
    mocker.patch("wagtail_resume.views.HTML")
    resume.pdf_generation_visibility = "authenticated"
    site.root_page.add_child(instance=resume)
    # Test random page pdf generation
    url = f"{reverse('generate_resume_pdf')}?page_id={resume.id}"
    request = rf.get(url)
    username = "user1"
    password = "bar"
    user = django_user_model.objects.create_user(username=username, password=password)

    request.user = user

    res = resume_pdf(request)
    print(res)
    assert "adin-hodovic" in res["content-disposition"]
    assert res.status_code == 200
    assert res["content-type"] == "application/pdf"


def test_weasyprint_disabled(site, resume, client, mocker):
    mocker.patch("wagtail_resume.views.HTML")
    resume.pdf_generation_visibility = "never"
    site.root_page.add_child(instance=resume)
    # Test random page pdf generation
    url = f"{reverse('generate_resume_pdf')}?page_id={resume.id}"
    res = client.get(url)
    assert b"<h1>PDF generation is disabled for this resume.</h1>" in res.content
    assert res.status_code == 400


def test_weasyprint_with_no_page_id(site, resume, client, mocker):
    mocker.patch("wagtail_resume.views.HTML")
    site.root_page.add_child(instance=resume)
    # Test random page pdf generation
    url = f"{reverse('generate_resume_pdf')}"
    res = client.get(url)
    assert b"Missing page id for resume generation" in res.content
    assert res.status_code == 400


def test_weasyprint_with_no_number(site, resume, client, mocker):
    mocker.patch("wagtail_resume.views.HTML")
    site.root_page.add_child(instance=resume)
    # Test random page pdf generation
    url = f"{reverse('generate_resume_pdf')}?page_id={resume.id}'"
    res = client.get(url)
    assert b"Page id is not a number" in res.content
    assert res.status_code == 400


def test_weasyprint_no_resume(site, resume, client, mocker):
    mocker.patch("wagtail_resume.views.HTML")
    site.root_page.add_child(instance=resume)
    # Test non existent resume
    url = f"{reverse('generate_resume_pdf')}?page_id=9999"
    res = client.get(url)
    assert res.status_code == 404


def test_weasyprint_logger_warnings_disabled():
    logger = logging.getLogger("weasyprint")
    assert logger.level == 40


def test_academic_resume_pdf(site, resume, client, mocker):
    mocker.patch("wagtail_resume.views.HTML")

    resume.pdf_generation_visibility = "always"

    site.root_page.add_child(instance=resume)
    # Test academic resume pdf generation
    url = f"{reverse('generate_academic_resume_pdf')}?page_id={resume.id}"
    res = client.get(url)
    assert "adin-hodovic" in res["content-disposition"]
    assert "academic-resume" in res["content-disposition"]
    assert res.status_code == 200
    assert res["content-type"] == "application/pdf"


def test_academic_resume_pdf_unauthenticated(resume, site, client, mocker):
    mocker.patch("wagtail_resume.views.HTML")
    resume.pdf_generation_visibility = "authenticated"
    site.root_page.add_child(instance=resume)
    # Test academic resume pdf generation
    url = f"{reverse('generate_academic_resume_pdf')}?page_id={resume.id}"
    res = client.get(url)
    assert b"You need to be authenticated to generate a resume PDF file." in res.content
    assert res.status_code == 403


def test_academic_resume_pdf_authenticated(site, resume, rf, django_user_model, mocker):
    mocker.patch("wagtail_resume.views.HTML")
    resume.pdf_generation_visibility = "authenticated"
    site.root_page.add_child(instance=resume)
    # Test academic resume pdf generation
    url = f"{reverse('generate_academic_resume_pdf')}?page_id={resume.id}"
    request = rf.get(url)
    username = "user1"
    password = "bar"
    user = django_user_model.objects.create_user(username=username, password=password)

    request.user = user

    res = academic_resume_pdf(request)
    assert "adin-hodovic" in res["content-disposition"]
    assert "academic-resume" in res["content-disposition"]
    assert res.status_code == 200
    assert res["content-type"] == "application/pdf"


def test_academic_resume_pdf_disabled(site, resume, client, mocker):
    mocker.patch("wagtail_resume.views.HTML")
    resume.pdf_generation_visibility = "never"
    site.root_page.add_child(instance=resume)
    # Test academic resume pdf generation
    url = f"{reverse('generate_academic_resume_pdf')}?page_id={resume.id}"
    res = client.get(url)
    assert b"<h1>PDF generation is disabled for this resume.</h1>" in res.content
    assert res.status_code == 400


def test_academic_resume_pdf_with_no_page_id(site, resume, client, mocker):
    mocker.patch("wagtail_resume.views.HTML")
    site.root_page.add_child(instance=resume)
    # Test academic resume pdf generation
    url = f"{reverse('generate_academic_resume_pdf')}"
    res = client.get(url)
    assert b"Missing page id for resume generation" in res.content
    assert res.status_code == 400


def test_academic_resume_pdf_with_no_number(site, resume, client, mocker):
    mocker.patch("wagtail_resume.views.HTML")
    site.root_page.add_child(instance=resume)
    # Test academic resume pdf generation
    url = f"{reverse('generate_academic_resume_pdf')}?page_id={resume.id}'"
    res = client.get(url)
    assert b"Page id is not a number" in res.content
    assert res.status_code == 400


def test_academic_resume_pdf_no_resume(site, resume, client, mocker):
    mocker.patch("wagtail_resume.views.HTML")
    site.root_page.add_child(instance=resume)
    # Test non existent resume
    url = f"{reverse('generate_academic_resume_pdf')}?page_id=9999"
    res = client.get(url)
    assert res.status_code == 404
