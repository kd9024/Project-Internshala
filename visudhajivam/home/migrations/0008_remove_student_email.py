# Generated by Django 2.2.6 on 2021-06-21 11:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_auto_20210621_1623'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='email',
        ),
    ]
