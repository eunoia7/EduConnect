# Generated by Django 3.2.6 on 2022-07-17 07:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0005_notes'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Notes',
        ),
    ]