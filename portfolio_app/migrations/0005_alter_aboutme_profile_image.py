# Generated by Django 5.1.3 on 2024-11-26 07:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio_app', '0004_remove_aboutme_avatar_remove_project_technology_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aboutme',
            name='profile_image',
            field=models.ImageField(blank=True, null=True, upload_to='profile_images'),
        ),
    ]
