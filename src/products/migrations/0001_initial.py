# Generated by Django 2.0.7 on 2019-08-03 07:05

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('ID', models.AutoField(primary_key=True, serialize=False)),
                ('URL', models.TextField()),
                ('DIV_ID', models.CharField(max_length=120)),
                ('Email', models.CharField(max_length=120, validators=[django.core.validators.EmailValidator()])),
                ('Active', models.BooleanField(default=True)),
                ('Price', models.IntegerField()),
            ],
        ),
    ]
