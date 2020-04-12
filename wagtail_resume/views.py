import datetime
import logging

from django.http import HttpResponse
from weasyprint import HTML

from wagtail_resume.templatetags.wagtail_resume_extras import space_to_plus

logger = logging.getLogger("weasyprint")
logger.addHandler(logging.NullHandler())
logger.setLevel(40) # Only show errors, use 50


def resume_pdf(request):
    response = HttpResponse(content_type="application/pdf")
    name = request.GET.get("name")
    response[
        "Content-Disposition"
    ] = "inline; filename={name}-resume-{date}.pdf".format(
        name=name, date=datetime.datetime.now().strftime("%Y-%m-%d"),
    )

    font = request.GET.get("font")
    if font:
        font = space_to_plus(font)
        HTML(url=request.GET.get("resume_url")).write_pdf(
            response,
            stylesheets=[
                # pylint: disable=line-too-long
                f"https://fonts.googleapis.com/css?family={font}&display=swap"
            ],
        )
    else:
        HTML(url=request.GET.get("resume_url")).write_pdf(response)
    return response
