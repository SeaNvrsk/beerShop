# Generated by Django 4.0.4 on 2022-06-23 21:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_remove_userprofile_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='birthDay',
            field=models.DateField(help_text='формат: 12.05.1990', null=True, verbose_name='День рождения'),
        ),
    ]