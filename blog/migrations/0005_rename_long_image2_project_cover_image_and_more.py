# Generated by Django 5.0.3 on 2024-03-11 21:01

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("blog", "0004_alter_article_options_article_created_at"),
    ]

    operations = [
        migrations.RenameField(
            model_name="project",
            old_name="long_image2",
            new_name="cover_image",
        ),
        migrations.RenameField(
            model_name="project",
            old_name="short_image1",
            new_name="detail_image",
        ),
        migrations.RenameField(
            model_name="project",
            old_name="long_image1",
            new_name="intro_image",
        ),
        migrations.RenameField(
            model_name="project",
            old_name="short_image2",
            new_name="outro_image",
        ),
    ]