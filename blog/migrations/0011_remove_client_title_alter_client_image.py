# Generated by Django 5.0.3 on 2024-03-30 12:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0010_client_title"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="client",
            name="title",
        ),
        migrations.AlterField(
            model_name="client",
            name="image",
            field=models.ImageField(upload_to="projects/"),
        ),
    ]
