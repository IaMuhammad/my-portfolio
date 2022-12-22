# Generated by Django 4.1.4 on 2022-12-21 14:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0005_remove_user_skill_skills_user'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Skills',
            new_name='Skill',
        ),
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('timedelta', models.CharField(max_length=20)),
                ('place', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=255)),
            ],
        ),
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'Category', 'verbose_name_plural': 'Categories'},
        ),
    ]