# Generated by Django 4.2.2 on 2023-06-27 21:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_alter_branch_data_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='branch_data',
            name='No',
        ),
        migrations.AddField(
            model_name='branch_data',
            name='Sno',
            field=models.IntegerField(default=1),
        ),
    ]
