import datetime
import logging

from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseNotFound
from django.utils.text import slugify
from wagtail.core.models import Page
from weasyprint import HTML

from wagtail_resume.templatetags.wagtail_resume_extras import space_to_plus

logger = logging.getLogger("weasyprint")
logger.addHandler(logging.NullHandler())
logger.setLevel(40)  # Only show errors, use 50


def resume_pdf(request):

    page_id = request.GET.get("page_id")
    if not page_id:
        return HttpResponseBadRequest("Missing page id for resume generation")
    response = HttpResponse(content_type="application/pdf")
    resume = Page.objects.filter(id=page_id).first()

    if not resume:
        return HttpResponseNotFound("<h1>Page not found</h1>")

    specific = resume.specific

    resume_url = specific.full_url
    name = slugify(specific.full_name)
    font = specific.font

    response[
        "Content-Disposition"
    ] = "inline; filename={name}-resume-{date}.pdf".format(
        name=name,
        date=datetime.datetime.now().strftime("%Y-%m-%d"),
    )

    if font:
        font = space_to_plus(font).title()
        HTML(url=resume_url).write_pdf(
            response,
            stylesheets=[
                # pylint: disable=line-too-long
                f"https://fonts.googleapis.com/css?family={font}&display=swap"
            ],
        )
    else:
        HTML(url=resume_url).write_pdf(response)
    return response
