import pytest
from wagtail.core.models import Site

from .models import CustomResumePage

pytestmark = pytest.mark.django_db


def test_translations(client):

    site = Site.objects.first()
    resume = CustomResumePage(
        title="Resume",
        full_name="Adin Hodovic",
        role="Software engineer",
    )
    site.root_page.add_child(instance=resume)
    content = client.get(resume.full_url, HTTP_ACCEPT_LANGUAGE="sv").content.decode(
        "utf-8"
    )

    assert "Om" in content
    assert "About" not in content

    assert "Hämta PDF" in content
    assert "Get PDF" not in content
