# Generated by Django 2.0.2 on 2018-07-26 12:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('olimpiada', '0013_auto_20180726_1237'),
    ]

    operations = [
        migrations.AddField(
            model_name='teacher',
            name='obj_state',
            field=models.CharField(blank=True, max_length=50, verbose_name='Status obiektu'),
        ),
    ]
