# Generated by Django 4.0.4 on 2022-06-25 10:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_alter_product_container_alter_product_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='slug',
            field=models.SlugField(default=1, max_length=250, unique=True, verbose_name='URL'),
            preserve_default=False,
        ),
    ]
