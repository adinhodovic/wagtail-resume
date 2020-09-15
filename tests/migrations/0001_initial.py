# Generated by Django 2.2.9 on 2019-12-26 11:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("wagtail_resume", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="CustomResumePage",
            fields=[
                (
                    "baseresumepage_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="wagtail_resume.BaseResumePage",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
            bases=("wagtail_resume.baseresumepage",),
        ),
    ]
