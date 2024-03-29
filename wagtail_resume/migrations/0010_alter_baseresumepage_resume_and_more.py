# Generated by Django 4.1.2 on 2023-05-13 17:34

from django.db import migrations
import wagtail.blocks
import wagtail.fields
import wagtail.images.blocks
import wagtailmarkdown.blocks


class Migration(migrations.Migration):

    dependencies = [
        ("wagtail_resume", "0009_alter_baseresumepage_pdf_generation_visibility"),
    ]

    operations = [
        migrations.AlterField(
            model_name="baseresumepage",
            name="resume",
            field=wagtail.fields.StreamField(
                [
                    (
                        "work_experience",
                        wagtail.blocks.StructBlock(
                            [
                                (
                                    "heading",
                                    wagtail.blocks.CharBlock(default="Work experience"),
                                ),
                                (
                                    "fa_icon",
                                    wagtail.blocks.CharBlock(default="fas fa-tools"),
                                ),
                                (
                                    "experiences",
                                    wagtail.blocks.ListBlock(
                                        wagtail.blocks.StructBlock(
                                            [
                                                ("role", wagtail.blocks.CharBlock()),
                                                ("company", wagtail.blocks.CharBlock()),
                                                ("url", wagtail.blocks.URLBlock()),
                                                (
                                                    "location",
                                                    wagtail.blocks.CharBlock(
                                                        required=False
                                                    ),
                                                ),
                                                (
                                                    "from_date",
                                                    wagtail.blocks.DateBlock(),
                                                ),
                                                (
                                                    "to_date",
                                                    wagtail.blocks.DateBlock(
                                                        required=False
                                                    ),
                                                ),
                                                (
                                                    "currently_working_here",
                                                    wagtail.blocks.BooleanBlock(
                                                        help_text="Check this box if you are currently working here and it will indicate so on the resume.",
                                                        required=False,
                                                    ),
                                                ),
                                                (
                                                    "text",
                                                    wagtailmarkdown.blocks.MarkdownBlock(),
                                                ),
                                            ],
                                            icon="folder-open-inverse",
                                        )
                                    ),
                                ),
                            ]
                        ),
                    ),
                    (
                        "contributions",
                        wagtail.blocks.StructBlock(
                            [
                                (
                                    "heading",
                                    wagtail.blocks.CharBlock(default="Contributions"),
                                ),
                                (
                                    "fa_icon",
                                    wagtail.blocks.CharBlock(
                                        default="fas fa-code-branch"
                                    ),
                                ),
                                (
                                    "contributions",
                                    wagtail.blocks.ListBlock(
                                        wagtail.blocks.StructBlock(
                                            [
                                                ("title", wagtail.blocks.CharBlock()),
                                                (
                                                    "description",
                                                    wagtail.blocks.TextBlock(),
                                                ),
                                                ("url", wagtail.blocks.URLBlock()),
                                            ],
                                            icon="folder-open-inverse",
                                        )
                                    ),
                                ),
                            ]
                        ),
                    ),
                    (
                        "writing",
                        wagtail.blocks.StructBlock(
                            [
                                (
                                    "heading",
                                    wagtail.blocks.CharBlock(default="Writing"),
                                ),
                                (
                                    "fa_icon",
                                    wagtail.blocks.CharBlock(
                                        default="fas fa-pencil-alt"
                                    ),
                                ),
                                (
                                    "posts",
                                    wagtail.blocks.StreamBlock(
                                        [
                                            (
                                                "internal_post",
                                                wagtail.blocks.StructBlock(
                                                    [
                                                        (
                                                            "post",
                                                            wagtail.blocks.PageChooserBlock(),
                                                        )
                                                    ],
                                                    icon="doc-full-inverse",
                                                ),
                                            ),
                                            (
                                                "external_post",
                                                wagtail.blocks.StructBlock(
                                                    [
                                                        (
                                                            "title",
                                                            wagtail.blocks.CharBlock(),
                                                        ),
                                                        (
                                                            "url",
                                                            wagtail.blocks.URLBlock(),
                                                        ),
                                                        (
                                                            "date",
                                                            wagtail.blocks.DateBlock(),
                                                        ),
                                                    ],
                                                    icon="doc-full-inverse",
                                                ),
                                            ),
                                        ],
                                        icon="folder-open-inverse",
                                    ),
                                ),
                            ]
                        ),
                    ),
                    (
                        "education",
                        wagtail.blocks.StructBlock(
                            [
                                (
                                    "heading",
                                    wagtail.blocks.CharBlock(default="Education"),
                                ),
                                (
                                    "fa_icon",
                                    wagtail.blocks.CharBlock(
                                        default="fas fa-graduation-cap"
                                    ),
                                ),
                                (
                                    "educations",
                                    wagtail.blocks.StreamBlock(
                                        [
                                            (
                                                "degree",
                                                wagtail.blocks.StructBlock(
                                                    [
                                                        (
                                                            "degree",
                                                            wagtail.blocks.CharBlock(
                                                                default="Bachelor's degree"
                                                            ),
                                                        ),
                                                        (
                                                            "field_of_study",
                                                            wagtail.blocks.CharBlock(
                                                                default="Computer Software Engineering"
                                                            ),
                                                        ),
                                                        (
                                                            "degree_url",
                                                            wagtail.blocks.URLBlock(),
                                                        ),
                                                        (
                                                            "university_name",
                                                            wagtail.blocks.CharBlock(),
                                                        ),
                                                        (
                                                            "university_url",
                                                            wagtail.blocks.URLBlock(),
                                                        ),
                                                        (
                                                            "studies_starting_date",
                                                            wagtail.blocks.DateBlock(
                                                                help_text="The year will only be displayed in the resume"
                                                            ),
                                                        ),
                                                        (
                                                            "studies_ending_date",
                                                            wagtail.blocks.DateBlock(
                                                                help_text="The year will only be displayed in the resume"
                                                            ),
                                                        ),
                                                    ],
                                                    icon="doc-full-inverse",
                                                ),
                                            ),
                                            (
                                                "certificate",
                                                wagtail.blocks.StructBlock(
                                                    [
                                                        (
                                                            "name",
                                                            wagtail.blocks.CharBlock(),
                                                        ),
                                                        (
                                                            "certificate_url",
                                                            wagtail.blocks.URLBlock(),
                                                        ),
                                                        (
                                                            "studies_starting_date",
                                                            wagtail.blocks.DateBlock(
                                                                help_text="The year and month will only be displayed in the resume"
                                                            ),
                                                        ),
                                                        (
                                                            "studies_ending_date",
                                                            wagtail.blocks.DateBlock(
                                                                help_text="The year and month will only be displayed in the resume"
                                                            ),
                                                        ),
                                                        (
                                                            "institute_name",
                                                            wagtail.blocks.CharBlock(),
                                                        ),
                                                        (
                                                            "institute_url",
                                                            wagtail.blocks.URLBlock(),
                                                        ),
                                                    ],
                                                    icon="doc-full-inverse",
                                                ),
                                            ),
                                            (
                                                "course",
                                                wagtail.blocks.StructBlock(
                                                    [
                                                        (
                                                            "name",
                                                            wagtail.blocks.CharBlock(),
                                                        ),
                                                        (
                                                            "course_url",
                                                            wagtail.blocks.URLBlock(),
                                                        ),
                                                        (
                                                            "studies_starting_date",
                                                            wagtail.blocks.DateBlock(
                                                                help_text="The year and month will only be displayed in the resume"
                                                            ),
                                                        ),
                                                        (
                                                            "studies_ending_date",
                                                            wagtail.blocks.DateBlock(
                                                                help_text="The year and month will only be displayed in the resume"
                                                            ),
                                                        ),
                                                    ],
                                                    icon="doc-full-inverse",
                                                ),
                                            ),
                                        ]
                                    ),
                                ),
                            ]
                        ),
                    ),
                ],
                blank=True,
                null=True,
                use_json_field=True,
            ),
        ),
        migrations.AlterField(
            model_name="baseresumepage",
            name="social_links",
            field=wagtail.fields.StreamField(
                [
                    (
                        "social_link",
                        wagtail.blocks.StructBlock(
                            [
                                ("text", wagtail.blocks.TextBlock()),
                                ("url", wagtail.blocks.URLBlock()),
                                (
                                    "logo",
                                    wagtail.images.blocks.ImageChooserBlock(
                                        required=False
                                    ),
                                ),
                            ],
                            icon="group",
                        ),
                    )
                ],
                blank=True,
                null=True,
                use_json_field=True,
            ),
        ),
    ]
