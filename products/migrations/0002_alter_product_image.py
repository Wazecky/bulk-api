# Generated by Django 4.2.7 on 2024-03-18 21:31

from django.db import migrations, models
import products.models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(upload_to=products.models.get_image_path),
        ),
    ]
