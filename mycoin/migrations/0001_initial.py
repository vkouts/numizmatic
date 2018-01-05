# Generated by Django 2.0.1 on 2018-01-04 22:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('coin', '0002_auto_20180105_0151'),
    ]

    operations = [
        migrations.CreateModel(
            name='MyCoin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('state', models.CharField(blank=True, choices=[('UNC', 'UNC'), ('AUNC', 'AUNC'), ('XF', 'XF'), ('VF', 'VF'), ('F', 'F'), ('G', 'G')], max_length=5, null=True)),
                ('coin', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='coin.Coin')),
            ],
        ),
    ]
