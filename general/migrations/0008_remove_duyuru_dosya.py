# Generated by Django 3.0.5 on 2020-08-30 11:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('general', '0007_auto_20200830_1409'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='duyuru',
            name='dosya',
        ),
    ]
