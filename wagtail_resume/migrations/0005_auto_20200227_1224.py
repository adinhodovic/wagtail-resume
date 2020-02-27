# Generated by Django 2.2.9 on 2020-02-27 12:24

from django.db import migrations
import wagtail.core.blocks
import wagtail.core.fields
import wagtailmarkdown.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('wagtail_resume', '0004_auto_20200110_1656'),
    ]

    operations = [
        migrations.AlterField(
            model_name='baseresumepage',
            name='resume',
            field=wagtail.core.fields.StreamField([('work_experience', wagtail.core.blocks.StructBlock([('heading', wagtail.core.blocks.CharBlock(default='Work experience')), ('fa_icon', wagtail.core.blocks.CharBlock(default='fas fa-tools')), ('experiences', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('role', wagtail.core.blocks.CharBlock()), ('company', wagtail.core.blocks.CharBlock()), ('url', wagtail.core.blocks.URLBlock()), ('from_date', wagtail.core.blocks.DateBlock()), ('to_date', wagtail.core.blocks.DateBlock(required=False)), ('currently_working_here', wagtail.core.blocks.BooleanBlock(help_text='Check this box if you are currently working here and it will indicate so on the resume.', required=False)), ('text', wagtailmarkdown.blocks.MarkdownBlock())], icon='folder-open-inverse')))])), ('contributions', wagtail.core.blocks.StructBlock([('heading', wagtail.core.blocks.CharBlock(default='Contributions')), ('fa_icon', wagtail.core.blocks.CharBlock(default='fas fa-code-branch')), ('contributions', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock()), ('description', wagtail.core.blocks.TextBlock()), ('url', wagtail.core.blocks.URLBlock())], icon='folder-open-inverse')))])), ('writing', wagtail.core.blocks.StructBlock([('heading', wagtail.core.blocks.CharBlock(default='Writing')), ('fa_icon', wagtail.core.blocks.CharBlock(default='fas fa-pencil-alt')), ('posts', wagtail.core.blocks.StreamBlock([('internal_post', wagtail.core.blocks.StructBlock([('post', wagtail.core.blocks.PageChooserBlock())], icon='doc-full-inverse')), ('external_post', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock()), ('url', wagtail.core.blocks.URLBlock()), ('date', wagtail.core.blocks.DateBlock())], icon='doc-full-inverse'))], icon='folder-open-inverse'))])), ('education', wagtail.core.blocks.StructBlock([('heading', wagtail.core.blocks.CharBlock(default='Education')), ('fa_icon', wagtail.core.blocks.CharBlock(default='fas fa-graduation-cap')), ('educations', wagtail.core.blocks.StreamBlock([('degree', wagtail.core.blocks.StructBlock([('degree', wagtail.core.blocks.CharBlock(default="Bachelor's degree")), ('field_of_study', wagtail.core.blocks.CharBlock(default='Computer Software Engineering')), ('degree_url', wagtail.core.blocks.URLBlock()), ('university_name', wagtail.core.blocks.CharBlock()), ('university_url', wagtail.core.blocks.URLBlock()), ('studies_starting_date', wagtail.core.blocks.DateBlock(help_text='The year will only be displayed in the resume')), ('studies_ending_date', wagtail.core.blocks.DateBlock(help_text='The year will only be displayed in the resume'))], icon='doc-full-inverse')), ('certificate', wagtail.core.blocks.StructBlock([('name', wagtail.core.blocks.CharBlock()), ('certificate_url', wagtail.core.blocks.URLBlock()), ('studies_starting_date', wagtail.core.blocks.DateBlock(help_text='The year and month will only be displayed in the resume')), ('studies_ending_date', wagtail.core.blocks.DateBlock(help_text='The year and month will only be displayed in the resume')), ('institute_name', wagtail.core.blocks.CharBlock()), ('institute_url', wagtail.core.blocks.URLBlock())], icon='doc-full-inverse')), ('course', wagtail.core.blocks.StructBlock([('name', wagtail.core.blocks.CharBlock()), ('course_url', wagtail.core.blocks.URLBlock()), ('studies_starting_date', wagtail.core.blocks.DateBlock(help_text='The year and month will only be displayed in the resume')), ('studies_ending_date', wagtail.core.blocks.DateBlock(help_text='The year and month will only be displayed in the resume'))], icon='doc-full-inverse'))]))]))], blank=True, null=True),
        ),
    ]
