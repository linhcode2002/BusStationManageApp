# Generated by Django 5.0.3 on 2024-05-04 11:08

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('BusManage', '0005_remove_review_rating_comments'),
    ]

    operations = [
        migrations.AlterField(
            model_name='buscompany',
            name='avatar',
            field=cloudinary.models.CloudinaryField(max_length=255, null=True, verbose_name='avatar'),
        ),
    ]
