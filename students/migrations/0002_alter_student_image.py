# Generated by Django 5.0.6 on 2024-06-12 10:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='image',
            field=models.ImageField(default='students/defaultImage.png', upload_to='students/%Y/%m/%d/'),
        ),
    ]