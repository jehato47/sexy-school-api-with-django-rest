# Generated by Django 3.1.1 on 2020-09-17 19:50

from django.db import migrations, models
import general.models


class Migration(migrations.Migration):

    dependencies = [
        ('general', '0022_delete_duyurudosya'),
    ]

    operations = [
        migrations.AlterField(
            model_name='duyuru',
            name='dosya',
            field=models.FileField(null=True, upload_to='', validators=[general.models.file_control]),
        ),
    ]
