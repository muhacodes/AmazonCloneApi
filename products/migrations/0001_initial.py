# Generated by Django 4.0.8 on 2023-01-03 13:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=2000)),
                ('images', models.ImageField(upload_to='')),
                ('name', models.CharField(max_length=250)),
                ('price', models.DecimalField(decimal_places=2, max_digits=13)),
                ('quantity', models.SmallIntegerField()),
            ],
        ),
    ]
