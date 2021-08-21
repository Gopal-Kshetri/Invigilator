# Generated by Django 2.2.24 on 2021-08-21 14:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scheduling', '0002_auto_20210821_0945'),
        ('assigning', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='selection',
            name='selected_persons',
        ),
        migrations.AddField(
            model_name='selection',
            name='selected_persons',
            field=models.ManyToManyField(to='scheduling.Person'),
        ),
    ]