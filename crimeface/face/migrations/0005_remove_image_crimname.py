# Generated by Django 2.2.7 on 2020-02-11 11:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('face', '0004_image_crimname'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='image',
            name='CrimName',
        ),
    ]
