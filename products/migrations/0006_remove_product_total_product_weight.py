# Generated by Django 4.1.3 on 2022-11-17 21:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_remove_product_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='total',
        ),
        migrations.AddField(
            model_name='product',
            name='weight',
            field=models.IntegerField(blank=True, null=True, verbose_name='Weight (g)'),
        ),
    ]