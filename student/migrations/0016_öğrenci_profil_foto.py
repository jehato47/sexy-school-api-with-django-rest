# Generated by Django 3.1.1 on 2020-09-15 16:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0015_auto_20200913_1453'),
    ]

    operations = [
        migrations.AddField(
            model_name='öğrenci',
            name='profil_foto',
            field=models.FileField(null=True, upload_to=''),
        ),
    ]
