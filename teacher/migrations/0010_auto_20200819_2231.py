# Generated by Django 3.0.5 on 2020-08-19 19:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('teacher', '0009_delete_sınıf'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='etüt',
            name='user',
        ),
        migrations.DeleteModel(
            name='Yoklama',
        ),
        migrations.DeleteModel(
            name='Etüt',
        ),
    ]