# Generated by Django 2.2.24 on 2021-08-07 06:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=15, verbose_name='title')),
                ('date', models.DateField(verbose_name='date')),
                ('time', models.TimeField(verbose_name='time')),
            ],
        ),
    ]
