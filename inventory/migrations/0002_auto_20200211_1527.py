# Generated by Django 3.0.2 on 2020-02-11 15:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='History',
            new_name='Transactions',
        ),
    ]
