import datetime
import logging

from django.http import (
    HttpResponse,
    HttpResponseBadRequest,
    HttpResponseForbidden,
    HttpResponseNotFound,
)
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
    if not page_id.isnumeric():
        return HttpResponseBadRequest("Page id is not a number")

    response = HttpResponse(content_type="application/pdf")
    resume = Page.objects.filter(id=page_id).first()

    if not resume:
        return HttpResponseNotFound("<h1>Page not found</h1>")

    specific = resume.specific

    if specific.pdf_generation_visibility == "never":
        return HttpResponseBadRequest(
            "<h1>PDF generation is disabled for this resume.</h1>"
        )

    authenticated = False
    if "user" in request:
        authenticated = request.user.is_authenticated
    if not authenticated and specific.pdf_generation_visibility == "authenticated":
        return HttpResponseForbidden(
            "<h1>You need to be authenticated to generate a resume PDF file.</h1>"
        )

    resume_url = specific.full_url
    name = slugify(specific.full_name)
    date = datetime.datetime.now().strftime("%Y-%m-%d")
    font = specific.font

    response["Content-Disposition"] = f"inline; filename={name}-resume-{date}.pdf"
    if font:
        font = space_to_plus(font).title()
        HTML(url=resume_url).write_pdf(
            response,
            stylesheets=[
                # pylint: disable=line-too-long
                f"https://fonts.googleapis.com/css2?family={font}&display=swap"
            ],
        )
    else:
        HTML(url=resume_url).write_pdf(response)
    return response
