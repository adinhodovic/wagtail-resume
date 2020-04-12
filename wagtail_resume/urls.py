from django.urls import path

from .views import resume_pdf

urlpatterns = [
    path(r"generate", resume_pdf, name="generate_resume_pdf"),
]
