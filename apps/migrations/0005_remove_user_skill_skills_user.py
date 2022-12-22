# Generated by Django 4.1.4 on 2022-12-21 14:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0004_skills'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='skill',
        ),
        migrations.AddField(
            model_name='skills',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
