# Generated by Django 5.0.3 on 2024-05-04 17:24

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BusManage', '0006_alter_buscompany_avatar'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='review',
            options={},
        ),
        migrations.AlterUniqueTogether(
            name='review',
            unique_together={('user', 'bus_company')},
        ),
        migrations.AddField(
            model_name='review',
            name='rating',
            field=models.IntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)]),
        ),
        migrations.RemoveField(
            model_name='review',
            name='comment',
        ),
    ]