# Generated by Django 2.2.9 on 2020-01-21 04:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_auto_20200121_0335'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='is_apply',
            field=models.BooleanField(default=False),
        ),
    ]