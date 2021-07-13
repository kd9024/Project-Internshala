# Generated by Django 2.2.6 on 2021-06-18 12:50

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_auto_20210618_0321'),
    ]

    operations = [
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('order_id', models.AutoField(primary_key=True, serialize=False)),
                ('amount', models.IntegerField(default=0)),
                ('name', models.CharField(max_length=90)),
                ('email', models.CharField(default='', max_length=111)),
                ('phone', models.CharField(default='', max_length=12)),
                ('image', models.ImageField(upload_to='img')),
                ('timeStamp', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]
