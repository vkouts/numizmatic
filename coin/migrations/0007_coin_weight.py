# Generated by Django 2.0.1 on 2018-01-05 21:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coin', '0006_coin_tags'),
    ]

    operations = [
        migrations.AddField(
            model_name='coin',
            name='weight',
            field=models.FloatField(default=0.0, verbose_name='Масса'),
        ),
    ]
