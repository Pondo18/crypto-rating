# Generated by Django 4.0 on 2021-12-22 08:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crypto', '0006_analysedscores'),
    ]

    operations = [
        migrations.AddField(
            model_name='analysedscores',
            name='score',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]