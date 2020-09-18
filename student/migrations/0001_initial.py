# Generated by Django 3.0.5 on 2020-07-16 13:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Öğrenci',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('isim', models.CharField(max_length=100)),
                ('soyisim', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100)),
                ('no', models.IntegerField(unique=True)),
                ('sınıf', models.IntegerField()),
                ('sınavsonuçları', models.CharField(blank=True, max_length=300, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]