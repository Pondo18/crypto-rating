# Generated by Django 4.0 on 2021-12-22 08:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('crypto', '0005_alter_currencies_rank'),
    ]

    operations = [
        migrations.CreateModel(
            name='AnalysedScores',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now_add=True)),
                ('crypto_currency', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crypto.currencies')),
            ],
        ),
    ]