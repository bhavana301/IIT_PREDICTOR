# Generated by Django 4.2.2 on 2023-06-28 16:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_alter_branch_data_gender'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='branch_data',
            new_name='Record',
        ),
    ]
