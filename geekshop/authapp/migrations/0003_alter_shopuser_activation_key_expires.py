# Generated by Django 3.2.4 on 2021-07-30 07:43

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0002_alter_shopuser_activation_key_expires'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shopuser',
            name='activation_key_expires',
            field=models.DateTimeField(default=datetime.datetime(2021, 8, 1, 7, 43, 44, 584020)),
        ),
    ]