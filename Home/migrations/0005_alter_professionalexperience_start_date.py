# Generated by Django 4.2.4 on 2023-08-26 17:19

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("Home", "0004_about_user_skill_user"),
    ]

    operations = [
        migrations.AlterField(
            model_name="professionalexperience",
            name="start_date",
            field=models.DateField(null=True, verbose_name="Start Date"),
        ),
    ]