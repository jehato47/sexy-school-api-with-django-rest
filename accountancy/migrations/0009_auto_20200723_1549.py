# Generated by Django 3.0.5 on 2020-07-23 12:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accountancy', '0008_muhasebe_ödenme_zamanları'),
    ]

    operations = [
        migrations.RenameField(
            model_name='muhasebe',
            old_name='ödenme_zamanları',
            new_name='ödeme_geçmişi',
        ),
    ]
