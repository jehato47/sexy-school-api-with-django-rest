# Generated by Django 2.2.4 on 2020-09-23 12:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0004_auto_20200923_1422'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ödev',
            name='image_field',
            field=models.FilePathField(blank=True, null=True),
        ),
    ]
