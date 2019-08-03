# Generated by Django 2.0.7 on 2019-08-03 16:27

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_product_user_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='Email',
            field=models.CharField(blank=True, max_length=120, null=True, validators=[django.core.validators.EmailValidator()]),
        ),
    ]
