import pytest
from bs4 import BeautifulSoup
from wagtail.core.models import Site

from .models import CustomResumePage

pytestmark = pytest.mark.django_db


def test_meta(client):
    site = Site.objects.first()
    resume = CustomResumePage(
        title="Resume",
        full_name="Adin Hodovic",
        role="Software engineer",
        about="This is a test",
    )
    site.root_page.add_child(instance=resume)
    res = client.get(resume.full_url)
    soup = BeautifulSoup(res.content, "html.parser")

    description = soup.find("meta", attrs={"name": "description"})
    assert (
        description["content"] == f"{resume.full_name} - {resume.role}. {resume.about}"
    )

    url = soup.find("meta", attrs={"itemprop": "url"})
    assert url["content"] == resume.get_full_url()

    title = soup.find("title")
    assert title.text == resume.full_name
