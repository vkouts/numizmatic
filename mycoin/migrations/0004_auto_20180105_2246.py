# Generated by Django 2.0.1 on 2018-01-05 19:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mycoin', '0003_auto_20180105_1200'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mycoinimage',
            name='image',
            field=models.ImageField(upload_to='mycoins/%Y/%m/%d/'),
        ),
    ]