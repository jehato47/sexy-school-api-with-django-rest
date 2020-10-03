# Generated by Django 2.2.4 on 2020-09-23 11:22

from django.db import migrations, models
import management.models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0003_auto_20200909_1430'),
    ]

    operations = [
        migrations.AddField(
            model_name='ödev',
            name='dosya',
            field=models.FileField(blank=True, null=True, upload_to='', validators=[management.models.file_control]),
        ),
        migrations.AddField(
            model_name='ödev',
            name='image_field',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
    ]