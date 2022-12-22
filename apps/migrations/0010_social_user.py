# Generated by Django 4.1.4 on 2022-12-21 15:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0009_remove_user_social_accs'),
    ]

    operations = [
        migrations.AddField(
            model_name='social',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]