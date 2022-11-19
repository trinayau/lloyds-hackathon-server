# Generated by Django 4.1.3 on 2022-11-17 21:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_remove_product_total_product_weight'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='emissions',
            field=models.DecimalField(decimal_places=2, max_digits=6, verbose_name='CO2'),
        ),
        migrations.AlterField(
            model_name='product',
            name='weight',
            field=models.IntegerField(blank=True, null=True, verbose_name='Weight (kg)'),
        ),
    ]