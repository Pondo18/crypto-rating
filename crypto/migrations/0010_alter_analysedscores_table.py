# Generated by Django 4.0 on 2021-12-24 13:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crypto', '0009_alter_analysedscores_options'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='analysedscores',
            table='crypto_analysed_scores',
        ),
    ]
