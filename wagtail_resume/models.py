from django.db import models
from wagtail.admin.edit_handlers import FieldPanel, MultiFieldPanel, StreamFieldPanel
from wagtail.core import blocks, fields
from wagtail.core.models import Page
from wagtail.images.blocks import ImageChooserBlock
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.images.models import Image
from wagtailmarkdown.edit_handlers import MarkdownPanel
from wagtailmarkdown.fields import MarkdownField
from wagtailmetadata.models import MetadataMixin

from .blocks import ContributionsBlock, WorkExperienceBlock, WritingsBlock


class ResumePage(MetadataMixin, Page):
    is_creatable = False
    template = "wagtail_resume/resume_page.html"

    full_name = models.CharField(max_length=100, null=True, blank=True)
    role = models.CharField(max_length=100, null=True, blank=True)
    about = MarkdownField(max_length=1000, null=True, blank=True)
    photo = models.ForeignKey(
        Image, null=True, blank=True, on_delete=models.SET_NULL, related_name="+"
    )
    social_links = fields.StreamField(
        [
            (
                "social_link",
                blocks.StructBlock(
                    [("url", blocks.URLBlock()), ("logo", ImageChooserBlock())]
                ),
            ),
        ],
        null=True,
        blank=True,
    )

    resume = fields.StreamField(
        [
            ("work_experience", WorkExperienceBlock()),
            ("contributions", ContributionsBlock()),
            ("writing", WritingsBlock()),
        ],
        null=True,
        blank=True,
    )

    content_panels = Page.content_panels + [
        MultiFieldPanel(
            [
                FieldPanel("full_name"),
                FieldPanel("role"),
                MarkdownPanel("about"),
                ImageChooserPanel("photo"),
                StreamFieldPanel("social_links"),
            ],
            heading="Personal details",
        ),
        StreamFieldPanel("resume"),
    ]

    def get_meta_title(self):
        return self.full_name

    def get_meta_description(self):
        return f"{self.full_name} - {self.role}"

    def get_meta_image(self):
        return self.photo

    def get_meta_url(self):
        return self.get_full_url
