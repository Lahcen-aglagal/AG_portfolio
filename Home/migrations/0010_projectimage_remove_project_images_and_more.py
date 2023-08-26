# Generated by Django 4.2.4 on 2023-08-26 20:13

import Home.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("Home", "0009_image_remove_project_image_project_images"),
    ]

    operations = [
        migrations.CreateModel(
            name="ProjectImage",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "image",
                    models.ImageField(
                        upload_to=Home.models.image_upload_path, verbose_name="Image"
                    ),
                ),
            ],
        ),
        migrations.RemoveField(
            model_name="project",
            name="images",
        ),
        migrations.RemoveField(
            model_name="skill",
            name="description",
        ),
        migrations.DeleteModel(
            name="Image",
        ),
        migrations.AddField(
            model_name="projectimage",
            name="project",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="images",
                to="Home.project",
            ),
        ),
    ]