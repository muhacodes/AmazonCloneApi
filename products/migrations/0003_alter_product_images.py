# Generated by Django 4.0.8 on 2023-01-03 13:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_category_alter_product_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='images',
            field=models.TextField(max_length=5000),
        ),
    ]
