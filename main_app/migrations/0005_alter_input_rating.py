# Generated by Django 4.0.4 on 2022-05-25 16:34

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0004_remove_hostel_images_remove_input_image_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='input',
            name='rating',
            field=models.IntegerField(validators=[django.core.validators.MaxValueValidator(10), django.core.validators.MinValueValidator(0)]),
        ),
    ]
