# Generated by Django 3.1.5 on 2021-03-04 04:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_photo'),
    ]

    operations = [
        migrations.RenameField(
            model_name='photo',
            old_name='Photo',
            new_name='Pic',
        ),
    ]
