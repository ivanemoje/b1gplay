# Generated by Django 2.1.5 on 2019-02-04 19:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sports', '0002_auto_20190204_1932'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agent',
            name='name',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
