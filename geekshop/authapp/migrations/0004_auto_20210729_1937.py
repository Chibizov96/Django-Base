# Generated by Django 3.2.4 on 2021-07-29 19:37

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0003_auto_20210725_1644'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shopuser',
            name='activation_key_expires',
            field=models.DateTimeField(default=datetime.datetime(2021, 7, 31, 19, 37, 35, 70315)),
        ),
        migrations.AlterField(
            model_name='shopuser',
            name='age',
            field=models.PositiveIntegerField(default=18, null=True, verbose_name='возраст'),
        ),
    ]
