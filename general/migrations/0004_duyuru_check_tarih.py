# Generated by Django 3.0.5 on 2020-08-20 16:22

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('general', '0003_auto_20200819_2243'),
    ]

    operations = [
        migrations.AddField(
            model_name='duyuru',
            name='check_tarih',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]