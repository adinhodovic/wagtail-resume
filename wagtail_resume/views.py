import datetime
import logging
from pathlib import Path

from django.contrib.staticfiles import finders
from django.http import (
    HttpResponse,
    HttpResponseBadRequest,
    HttpResponseForbidden,
    HttpResponseNotFound,
)
from django.template.loader import render_to_string
from django.utils.text import slugify
from wagtail.models import Page
from weasyprint import CSS, HTML

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
    if hasattr(request, "user"):
        authenticated = request.user.is_authenticated
    if not authenticated and specific.pdf_generation_visibility == "authenticated":
        return HttpResponseForbidden(
            "<h1>You need to be authenticated to generate a resume PDF file.</h1>"
        )

    resume_url = specific.full_url
    name = slugify(specific.full_name)
    if resume.latest_revision_created_at:
        resume_date = resume.latest_revision_created_at
    else:
        resume_date = datetime.datetime.now()
    date = resume_date.strftime("%Y-%m-%d")
    font = specific.font

    response["Content-Disposition"] = f"inline; filename={name}-resume-{date}.pdf"
    if font:
        font = space_to_plus(font).title()
        full_font = f"{font}:bold|{font}:bold,bolditalic,italic"
    else:
        full_font = "Roboto+Condensed|Roboto+Condensed:bold,bolditalic,italic"

    HTML(url=resume_url).write_pdf(
        response,
        stylesheets=[
            # pylint: disable=line-too-long
            # We use the default CSS API from Google Fonts to load the font
            # CSS2 requires boldness specification for bold fonts
            f"https://fonts.googleapis.com/css?family={full_font}&display=swap",
        ],
    )
    return response


def academic_resume_pdf(request):
    """Generate academic-style PDF version of resume."""

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

    # Reuse existing pdf_generation_visibility setting
    if specific.pdf_generation_visibility == "never":
        return HttpResponseBadRequest(
            "<h1>PDF generation is disabled for this resume.</h1>"
        )

    authenticated = False
    if hasattr(request, "user"):
        authenticated = request.user.is_authenticated
    if not authenticated and specific.pdf_generation_visibility == "authenticated":
        return HttpResponseForbidden(
            "<h1>You need to be authenticated to generate a resume PDF file.</h1>"
        )

    name = slugify(specific.full_name)
    if resume.latest_revision_created_at:
        resume_date = resume.latest_revision_created_at
    else:
        resume_date = datetime.datetime.now()
    date = resume_date.strftime("%Y-%m-%d")

    response[
        "Content-Disposition"
    ] = f"inline; filename={name}-academic-resume-{date}.pdf"

    # Render the academic template directly (no custom fonts needed)
    html_content = render_to_string(
        "wagtail_resume/academic_resume_page.html", {"page": specific}
    )

    # Find the CSS file - try static finders first, then fallback to package path
    css_path = finders.find("wagtail_resume/css/academic_resume_page.css")
    if not css_path:
        # Fallback to package-relative path for when staticfiles aren't collected
        package_dir = Path(__file__).parent
        css_path = package_dir / "static/wagtail_resume/css/academic_resume_page.css"

    stylesheets = [CSS(filename=str(css_path))] if css_path else []

    HTML(string=html_content, base_url=request.build_absolute_uri("/")).write_pdf(
        response, stylesheets=stylesheets
    )

    return response
