# Generated by Django 3.1.5 on 2021-03-01 16:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_auto_20210301_2128'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='sno',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
