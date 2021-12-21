# Generated by Django 4.0 on 2021-12-21 19:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crypto', '0005_alter_currencies_rank'),
        ('reddit', '0002_alter_posts_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='posts',
            name='crypto_currency',
        ),
        migrations.AddField(
            model_name='posts',
            name='crypto_currency',
            field=models.ManyToManyField(to='crypto.Currencies'),
        ),
    ]
