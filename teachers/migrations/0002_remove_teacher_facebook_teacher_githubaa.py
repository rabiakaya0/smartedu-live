# Generated by Django 5.0.6 on 2024-06-13 17:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teachers', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='teacher',
            name='facebook',
        ),
        migrations.AddField(
            model_name='teacher',
            name='githubaa',
            field=models.URLField(blank=True, max_length=100),
        ),
    ]
