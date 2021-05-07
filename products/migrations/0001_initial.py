# Generated by Django 2.2 on 2021-05-07 07:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(verbose_name='Дата')),
                ('title', models.CharField(max_length=50, verbose_name='Название')),
                ('description', models.CharField(max_length=1000, verbose_name='Содержание')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country', models.CharField(max_length=50, verbose_name='Страна')),
                ('state', models.CharField(max_length=50, verbose_name='Штат')),
                ('city', models.CharField(max_length=50, verbose_name='Город')),
                ('data', models.DateTimeField(verbose_name='Дата')),
                ('status', models.CharField(max_length=50, verbose_name='Статус')),
                ('number_track', models.CharField(max_length=50, verbose_name='Номер трека')),
                ('price', models.IntegerField()),
            ],
        ),
    ]
