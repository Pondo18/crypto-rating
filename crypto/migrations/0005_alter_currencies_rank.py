# Generated by Django 4.0 on 2021-12-17 10:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crypto', '0004_alter_currencies_slug_alter_currencies_symbol'),
    ]

    operations = [
        migrations.AlterField(
            model_name='currencies',
            name='rank',
            field=models.IntegerField(null=True),
        ),
    ]
