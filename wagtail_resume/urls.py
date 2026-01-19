from django.urls import path

from .views import academic_resume_pdf, resume_pdf

urlpatterns = [
    path(r"generate", resume_pdf, name="generate_resume_pdf"),
    path(
        r"generate-academic", academic_resume_pdf, name="generate_academic_resume_pdf"
    ),
]
