# pylint: disable=R0903,C0301
from wagtail import blocks
from wagtailmarkdown.blocks import MarkdownBlock


class WorkExperienceBlock(blocks.StructBlock):  # pragma: no cover
    class Meta:
        template = "wagtail_resume/blocks/work_experience_block.html"
        icon = "doc-full-inverse"

    def get_context(self, value, parent_context=None):
        context = super().get_context(value)
        max_exp = context["self"]["maximum_experiences_displayed"]
        experiences = context["self"]["experiences"]
        for index, experience in enumerate(experiences):
            if experience["hidden"] is True:
                experiences.pop(index)
        if max_exp > 0:
            exp_len = len(experiences)
            # Can't slice Wagtail's ListValue
            for _ in range(exp_len - max_exp):
                experiences.pop()

        context["self"]["experiences"] = experiences
        return context

    heading = blocks.CharBlock(default="Work experience")
    fa_icon = blocks.CharBlock(default="fas fa-tools", required=False)
    maximum_experiences_displayed = blocks.IntegerBlock(
        default=0,
        required=False,
        help_text="Set to 0 to show all experiences, otherwise set the maximum number of experiences to show.",
    )
    maximum_experiences_user_text = blocks.CharBlock(
        default="Only showing the most recent work experiences. All experiences can be shared on request.",
        required=False,
    )
    experiences = blocks.ListBlock(
        blocks.StructBlock(
            [
                ("role", blocks.CharBlock()),
                ("company", blocks.CharBlock()),
                ("hidden", blocks.BooleanBlock(required=False, default=False)),
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
    fa_icon = blocks.CharBlock(default="fas fa-pencil-alt", required=False)
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
    fa_icon = blocks.CharBlock(default="fas fa-code-branch", required=False)
    contributions = blocks.ListBlock(
        blocks.StructBlock(
            [
                ("title", blocks.CharBlock()),
                ("hidden", blocks.BooleanBlock(required=False, default=False)),
                ("description", blocks.TextBlock()),
                ("url", blocks.URLBlock()),
            ],
            icon="folder-open-inverse",
        )
    )

    def get_context(self, value, parent_context=None):
        context = super().get_context(value)
        contributions = context["self"]["contributions"]
        for index, contribution in enumerate(contributions):
            if contribution["hidden"] is True:
                contributions.pop(index)

        context["self"]["contributions"] = contributions
        return context


class EducationBlock(blocks.StructBlock):
    class Meta:
        template = "wagtail_resume/blocks/education_block.html"
        icon = "doc-full-inverse"

    heading = blocks.CharBlock(default="Education")
    fa_icon = blocks.CharBlock(default="fas fa-graduation-cap", required=False)
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
