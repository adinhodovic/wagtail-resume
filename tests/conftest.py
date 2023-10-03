import pytest
from wagtail.models import Site

from tests.models import CustomResumePage


@pytest.fixture
def resume():
    return CustomResumePage(
        title="Resume", full_name="Adin Hodovic", role="Software engineer"
    )


@pytest.fixture
def site():
    return Site.objects.first()
