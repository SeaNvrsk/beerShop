# Generated by Django 4.0.4 on 2022-06-02 15:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='quantity',
            field=models.PositiveIntegerField(default=0, verbose_name='количество'),
        ),
    ]
