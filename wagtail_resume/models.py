from django.db import models
from django.utils.text import Truncator
from wagtail.admin.edit_handlers import FieldPanel, MultiFieldPanel, StreamFieldPanel
from wagtail.core import blocks, fields
from wagtail.core.models import Page
from wagtail.images.blocks import ImageChooserBlock
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.images.models import Image
from wagtailmarkdown.edit_handlers import MarkdownPanel
from wagtailmarkdown.fields import MarkdownField
from wagtailmetadata.models import MetadataMixin

from .blocks import (
    ContributionsBlock,
    EducationBlock,
    WorkExperienceBlock,
    WritingsBlock,
)


class BaseResumePage(MetadataMixin, Page):
    page_ptr = models.OneToOneField(
        Page, parent_link=True, related_name="+", on_delete=models.CASCADE
    )
    is_creatable = False

    font = models.CharField(max_length=100, null=True, blank=True)
    background_color = models.CharField(max_length=100, null=True, blank=True)

    full_name = models.CharField(max_length=100, null=True, blank=True)

    pdf_generation_visibility = models.CharField(
        choices=(
            ("always", "Always visible"),
            ("authenticated", "Only logged in users"),
            ("never", "Never visible"),
        ),
        default="authenticated",
        help_text="""
            PDF generation is a heavy blocking operation,
            so it is recommended to only show it to logged in users. If available to everyone, ensure that you have multiple workers running.
        """,
        max_length=64,
    )

    role = models.CharField(max_length=100, null=True, blank=True)
    about = MarkdownField(max_length=2500, null=True, blank=True)
    photo = models.ForeignKey(
        Image, null=True, blank=True, on_delete=models.SET_NULL, related_name="+"
    )
    social_links = fields.StreamField(
        [
            (
                "social_link",
                blocks.StructBlock(
                    [
                        ("text", blocks.TextBlock()),
                        ("url", blocks.URLBlock()),
                        ("logo", ImageChooserBlock(required=False)),
                    ],
                    icon="group",
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
            ("education", EducationBlock()),
        ],
        null=True,
        blank=True,
    )

    content_panels = Page.content_panels + [
        MultiFieldPanel(
            [
                FieldPanel("font"),
                FieldPanel("background_color"),
                FieldPanel("pdf_generation_visibility"),
            ],
            heading="Customization",
        ),
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

    def get_template(self, request):  # pylint: disable=arguments-differ
        return "wagtail_resume/resume_page.html"

    def get_meta_title(self):
        return self.full_name

    def get_meta_description(self):
        about = Truncator(self.about).words(35)
        return f"{self.full_name} - {self.role}. {about}"

    def get_meta_image(self):
        return self.photo

    def get_meta_url(self):
        return self.get_full_url()

    def get_meta_twitter_card_type(self):
        return self.photo
