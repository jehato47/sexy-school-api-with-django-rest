# Generated by Django 3.0.5 on 2020-07-23 20:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accountancy', '0012_auto_20200723_2338'),
    ]

    operations = [
        migrations.AlterField(
            model_name='muhasebe',
            name='ilk_kayıt',
            field=models.DateField(auto_now_add=True),
        ),
    ]
