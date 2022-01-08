# Generated by Django 3.2.9 on 2022-01-08 06:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='newuser',
            managers=[
            ],
        ),
        migrations.AlterField(
            model_name='newuser',
            name='address',
            field=models.CharField(max_length=250, null=True, verbose_name='Address'),
        ),
        migrations.AlterField(
            model_name='newuser',
            name='city',
            field=models.CharField(max_length=100, null=True, verbose_name='City'),
        ),
        migrations.AlterField(
            model_name='newuser',
            name='id_number',
            field=models.IntegerField(null=True, unique=True, verbose_name='ID Number'),
        ),
        migrations.AlterField(
            model_name='newuser',
            name='job',
            field=models.CharField(max_length=100, null=True, verbose_name='Job'),
        ),
    ]