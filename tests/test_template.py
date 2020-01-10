import pytest
from bs4 import BeautifulSoup
from wagtail.core.models import Site

from .models import CustomResumePage

pytestmark = pytest.mark.django_db


def test_template(client):
    site = Site.objects.first()
    full_name = "Adin Hodovic"
    role = "Software engineer"
    about = "Full stack engineer with a preference for Django and DRF"
    resume = CustomResumePage(
        title="Resume", full_name=full_name, role=role, about=about
    )
    site.root_page.add_child(instance=resume)
    res = client.get(resume.full_url)
    soup = BeautifulSoup(res.content, "html.parser")

    template_name = soup.find("h2", {"class": "name"}).string
    assert template_name == full_name

    template_role = soup.find("h4", {"class": "role"}).string
    assert template_role == role

    template_about = soup.find("p", {"class": "about"})
    assert about in str(template_about)


def test_resume_preferences(client):
    site = Site.objects.first()
    resume = CustomResumePage(
        title="Resume",
        full_name="Adin Hodovic",
        role="Software engineer",
        font="lato",
        background_color="blue",
    )

    site.root_page.add_child(instance=resume)
    res = client.get(resume.full_url)
    soup = BeautifulSoup(res.content, "html.parser")

    template_body = soup.find("body")
    assert 'style="background: blue">' in str(template_body)
    assert "font-family: 'Lato'" in str(template_body)
