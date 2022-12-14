# Generated by Django 4.1.3 on 2022-12-14 09:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bludo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=24, verbose_name='name')),
            ],
        ),
        migrations.CreateModel(
            name='Zal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=24, verbose_name='name')),
            ],
        ),
        migrations.CreateModel(
            name='Zakaz',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fio', models.CharField(max_length=24, verbose_name='fio')),
                ('date', models.DateTimeField(verbose_name='date')),
                ('peoples', models.IntegerField(verbose_name='peoples')),
                ('soglas', models.BooleanField(verbose_name='soglas')),
                ('bludo', models.ManyToManyField(to='menu.bludo')),
                ('zal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='menu.zal')),
            ],
        ),
    ]