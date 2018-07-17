# Generated by Django 2.0.2 on 2018-07-10 12:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100, verbose_name='Imię')),
                ('last_name', models.CharField(max_length=100, verbose_name='Nazwisko')),
                ('position', models.CharField(max_length=100, verbose_name='Tytuł lub stopień zawodowy / naukowy')),
                ('phone_no', models.IntegerField(verbose_name='Telefon kontaktowy')),
            ],
            options={
                'verbose_name': 'Nauczyciel',
                'verbose_name_plural': 'Nauczyciele',
            },
        ),
    ]