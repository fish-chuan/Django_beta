# Generated by Django 2.2.9 on 2020-01-20 10:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='item_id',
            field=models.TextField(default='0000'),
        ),
    ]
