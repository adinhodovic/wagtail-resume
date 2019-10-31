from wagtail.core import blocks, fields
from wagtailmarkdown.blocks import MarkdownBlock


class WorkExperienceBlock(blocks.StructBlock):
    class Meta:
        template = "wagtail_resume/blocks/work_experience_block.html"

    heading = blocks.CharBlock(default="Work experience")
    fa_icon = blocks.CharBlock(default="fas fa-tools")
    experiences = blocks.ListBlock(
        blocks.StructBlock(
            [
                ("role", blocks.CharBlock()),
                ("company", blocks.CharBlock()),
                ("url", blocks.URLBlock()),
                ("from_date", blocks.DateBlock()),
                ("to_date", blocks.DateBlock()),
                ("text", MarkdownBlock()),
            ]
        )
    )


class WritingsBlock(blocks.StructBlock):
    class Meta:
        template = "wagtail_resume/blocks/writings_block.html"

    heading = blocks.CharBlock(default="Writing")
    fa_icon = blocks.CharBlock(default="fas fa-pencil-alt")
    posts = blocks.StreamBlock(
        [
            (
                "internal_post",
                blocks.StructBlock([("post", blocks.PageChooserBlock())]),
            ),
            (
                "external_post",
                blocks.StructBlock(
                    [
                        ("title", blocks.CharBlock()),
                        ("url", blocks.URLBlock()),
                        ("date", blocks.DateBlock()),
                    ]
                ),
            ),
        ]
    )


class ContributionsBlock(blocks.StructBlock):
    class Meta:
        template = "wagtail_resume/blocks/contributions_block.html"

    heading = blocks.CharBlock(default="Contributions")
    fa_icon = blocks.CharBlock(default="fab fa-github-square")
    contributions = blocks.ListBlock(
        blocks.StructBlock(
            [
                ("title", blocks.CharBlock(required=False)),
                ("description", blocks.TextBlock(required=False)),
                ("url", blocks.URLBlock(required=False)),
            ]
        )
    )
