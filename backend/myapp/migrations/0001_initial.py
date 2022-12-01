# Generated by Django 3.2.16 on 2022-11-30 10:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CryptoModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('price', models.DecimalField(decimal_places=10, max_digits=18)),
                ('perhour', models.DecimalField(decimal_places=2, max_digits=4)),
                ('day', models.DecimalField(decimal_places=2, max_digits=4)),
                ('week', models.DecimalField(decimal_places=2, max_digits=4)),
                ('marketcap', models.DecimalField(decimal_places=0, max_digits=12)),
                ('volume', models.DecimalField(decimal_places=0, max_digits=12)),
                ('cirulating_supply', models.CharField(max_length=250)),
            ],
        ),
    ]