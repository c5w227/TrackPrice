# Generated by Django 2.2.3 on 2019-08-04 15:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0008_remove_product_div_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='Email',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
    ]
