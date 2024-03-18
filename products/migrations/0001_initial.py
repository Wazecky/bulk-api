# Generated by Django 4.2.7 on 2024-03-18 20:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('image', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='ProductVariant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sku', models.CharField(max_length=50)),
                ('name', models.CharField(max_length=100)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('details', models.TextField()),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='variants', to='products.product')),
            ],
        ),
    ]
