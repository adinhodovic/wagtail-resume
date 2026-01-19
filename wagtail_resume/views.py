import datetime
import logging

from django.http import (
    HttpResponse,
    HttpResponseBadRequest,
    HttpResponseForbidden,
    HttpResponseNotFound,
)
from django.template.loader import render_to_string
from django.utils.text import slugify
from wagtail.models import Page
from weasyprint import HTML

from wagtail_resume.templatetags.wagtail_resume_extras import space_to_plus

logger = logging.getLogger("weasyprint")
logger.addHandler(logging.NullHandler())
logger.setLevel(40)  # Only show errors, use 50


def build_google_fonts_css(primary_font: str | None) -> str:
    """
    Build a Google Fonts CSS2 URL for WeasyPrint.

    Order:
    - primary_font (if provided)
    - Roboto (Latin/UI)
    - Noto Sans (broad Unicode coverage)
    - Noto Color Emoji (emoji)
    """
    weights = "0,400;0,500;0,600;0,700;1,400;1,500;1,600;1,700"

    def family_param(name: str, weighted: bool = True) -> str:
        name = space_to_plus(name.strip())
        if weighted:
            return f"family={name}:ital,wght@{weights}"
        return f"family={name}"

    parts = []

    if primary_font:
        parts.append(family_param(primary_font.title()))
        parts.append(family_param("Roboto"))
    else:
        parts.append(family_param("Roboto"))

    # Coverage fallback
    parts.append(family_param("Noto Sans"))

    # Emoji (no weights)
    parts.append(family_param("Noto Color Emoji", weighted=False))

    return "https://fonts.googleapis.com/css2?" + "&".join(parts) + "&display=swap"


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
    google_fonts_css = build_google_fonts_css(font)

    HTML(url=resume_url).write_pdf(
        response,
        stylesheets=[
            # pylint: disable=line-too-long
            # We use the default CSS API from Google Fonts to load the font
            # CSS2 requires boldness specification for bold fonts
            google_fonts_css
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

    # Get font from model
    font = specific.font

    google_fonts_css = build_google_fonts_css(font)

    # Render the academic template
    html_content = render_to_string(
        "wagtail_resume/academic_resume_page.html",
        {"page": specific},
    )

    HTML(string=html_content, base_url=request.build_absolute_uri("/"),).write_pdf(
        response,
        stylesheets=[google_fonts_css],
    )
    return response
