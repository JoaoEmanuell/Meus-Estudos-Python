# Generated by Django 3.2.9 on 2021-11-17 23:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contas', '0003_auto_20211117_2302'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transation',
            name='date',
            field=models.DateField(),
        ),
    ]
