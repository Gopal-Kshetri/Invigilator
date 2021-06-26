# Generated by Django 3.2.3 on 2021-06-26 07:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('page', '0006_auto_20210626_0706'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher',
            name='dob',
            field=models.DateField(blank=True, verbose_name='dob'),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='email_Id',
            field=models.EmailField(blank=True, max_length=254, verbose_name='email_Id'),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='gender',
            field=models.BooleanField(blank=True, verbose_name='gender'),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='middle_Name',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='photo',
            field=models.ImageField(blank=True, upload_to='', verbose_name='photo'),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='qualification',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]