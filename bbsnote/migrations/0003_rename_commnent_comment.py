# Generated by Django 3.2.9 on 2021-11-12 02:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bbsnote', '0002_rename_commnet_commnent'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Commnent',
            new_name='Comment',
        ),
    ]
