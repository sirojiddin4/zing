# Generated by Django 4.2.3 on 2023-07-07 13:35

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rating', '0004_rename_credits_credit_remove_group_students_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='credit',
            name='amount',
            field=models.PositiveIntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(4)]),
        ),
    ]
