# Generated by Django 4.0.6 on 2022-07-24 20:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='veiculos',
            name='created',
        ),
        migrations.RemoveField(
            model_name='veiculos',
            name='updated',
        ),
    ]