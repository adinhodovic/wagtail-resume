# pylint: disable=R0903,C0301
from wagtail.core import blocks
from wagtailmarkdown.blocks import MarkdownBlock


class WorkExperienceBlock(blocks.StructBlock):
    class Meta:
        template = "wagtail_resume/blocks/work_experience_block.html"
        icon = "doc-full-inverse"

    heading = blocks.CharBlock(default="Work experience")
    fa_icon = blocks.CharBlock(default="fas fa-tools")
    experiences = blocks.ListBlock(
        blocks.StructBlock(
            [
                ("role", blocks.CharBlock()),
                ("company", blocks.CharBlock()),
                ("url", blocks.URLBlock()),
                ("location", blocks.CharBlock(required=False)),
                ("from_date", blocks.DateBlock()),
                ("to_date", blocks.DateBlock(required=False)),
                (
                    "currently_working_here",
                    blocks.BooleanBlock(
                        help_text="Check this box if you are currently working here and it will indicate so on the resume.",
                        required=False,
                    ),
                ),
                ("text", MarkdownBlock()),
            ],
            icon="folder-open-inverse",
        )
    )


class WritingsBlock(blocks.StructBlock):
    class Meta:
        template = "wagtail_resume/blocks/writings_block.html"
        icon = "edit"

    heading = blocks.CharBlock(default="Writing")
    fa_icon = blocks.CharBlock(default="fas fa-pencil-alt")
    posts = blocks.StreamBlock(
        [
            (
                "internal_post",
                blocks.StructBlock(
                    [("post", blocks.PageChooserBlock())], icon="doc-full-inverse"
                ),
            ),
            (
                "external_post",
                blocks.StructBlock(
                    [
                        ("title", blocks.CharBlock()),
                        ("url", blocks.URLBlock()),
                        ("date", blocks.DateBlock()),
                    ],
                    icon="doc-full-inverse",
                ),
            ),
        ],
        icon="folder-open-inverse",
    )


class ContributionsBlock(blocks.StructBlock):
    class Meta:
        template = "wagtail_resume/blocks/contributions_block.html"
        icon = "code"

    heading = blocks.CharBlock(default="Contributions")
    fa_icon = blocks.CharBlock(default="fas fa-code-branch")
    contributions = blocks.ListBlock(
        blocks.StructBlock(
            [
                ("title", blocks.CharBlock()),
                ("description", blocks.TextBlock()),
                ("url", blocks.URLBlock()),
            ],
            icon="folder-open-inverse",
        )
    )


class EducationBlock(blocks.StructBlock):
    class Meta:
        template = "wagtail_resume/blocks/education_block.html"
        icon = "doc-full-inverse"

    heading = blocks.CharBlock(default="Education")
    fa_icon = blocks.CharBlock(default="fas fa-graduation-cap")
    educations = blocks.StreamBlock(
        [
            (
                "degree",
                blocks.StructBlock(
                    [
                        ("degree", blocks.CharBlock(default="Bachelor's degree")),
                        (
                            "field_of_study",
                            blocks.CharBlock(default="Computer Software Engineering"),
                        ),
                        ("degree_url", blocks.URLBlock()),
                        ("university_name", blocks.CharBlock()),
                        ("university_url", blocks.URLBlock()),
                        (
                            "studies_starting_date",
                            blocks.DateBlock(
                                help_text="The year will only be displayed in the resume"
                            ),
                        ),
                        (
                            "studies_ending_date",
                            blocks.DateBlock(
                                help_text="The year will only be displayed in the resume"
                            ),
                        ),
                    ],
                    icon="doc-full-inverse",
                ),
            ),
            (
                "certificate",
                blocks.StructBlock(
                    [
                        ("name", blocks.CharBlock()),
                        ("certificate_url", blocks.URLBlock()),
                        (
                            "studies_starting_date",
                            blocks.DateBlock(
                                help_text="The year and month will only be displayed in the resume"
                            ),
                        ),
                        (
                            "studies_ending_date",
                            blocks.DateBlock(
                                help_text="The year and month will only be displayed in the resume"
                            ),
                        ),
                        ("institute_name", blocks.CharBlock()),
                        ("institute_url", blocks.URLBlock()),
                    ],
                    icon="doc-full-inverse",
                ),
            ),
            (
                "course",
                blocks.StructBlock(
                    [
                        ("name", blocks.CharBlock()),
                        ("course_url", blocks.URLBlock()),
                        (
                            "studies_starting_date",
                            blocks.DateBlock(
                                help_text="The year and month will only be displayed in the resume"
                            ),
                        ),
                        (
                            "studies_ending_date",
                            blocks.DateBlock(
                                help_text="The year and month will only be displayed in the resume"
                            ),
                        ),
                    ],
                    icon="doc-full-inverse",
                ),
            ),
        ]
    )
