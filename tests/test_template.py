import pytest
from bs4 import BeautifulSoup

pytestmark = pytest.mark.django_db


def test_template(site, resume, client):
    about = "Full stack engineer with a preference for Django and DRF"
    resume.about = about
    site.root_page.add_child(instance=resume)
    res = client.get(resume.full_url)
    soup = BeautifulSoup(res.content, "html.parser")

    assert resume.full_name in soup.text

    assert resume.role in soup.text

    assert about in soup.text


def test_resume_preferences(site, resume, client):
    resume.font = "lato"
    resume.background_color = "blue"

    site.root_page.add_child(instance=resume)
    res = client.get(resume.full_url)
    soup = BeautifulSoup(res.content, "html.parser")

    template_body = soup.find("body")
    #  assert 'style="background: blue">' in str(template_body) TODO: Run test with media query pylint: disable=line-too-long
    assert "font-family: 'Lato'" in str(template_body)

    template_generate_pdf = soup.find("a", {"class": "pdf"})
    assert None is template_generate_pdf
