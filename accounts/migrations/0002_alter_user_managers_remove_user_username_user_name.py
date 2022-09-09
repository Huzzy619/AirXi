# Generated by Django 4.1 on 2022-09-08 10:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelManagers(
            name="user",
            managers=[],
        ),
        migrations.RemoveField(
            model_name="user",
            name="username",
        ),
        migrations.AddField(
            model_name="user",
            name="name",
            field=models.CharField(default="no_name", max_length=550),
            preserve_default=False,
        ),
    ]
