# Generated by Django 4.1 on 2022-09-02 09:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("airxiapp", "0006_booking_taxi_alter_booking_reference_number"),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name="contact",
            unique_together=set(),
        ),
    ]
