# Generated by Django 3.2.3 on 2021-06-26 06:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('page', '0004_auto_20210626_0648'),
    ]

    operations = [
        migrations.AlterField(
            model_name='staffs',
            name='phone_Num',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='students',
            name='phone_Num',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='teachers',
            name='phone_Num',
            field=models.CharField(max_length=10),
        ),
    ]