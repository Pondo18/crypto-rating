# Generated by Django 4.0 on 2021-12-24 13:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crypto', '0010_alter_analysedscores_table'),
    ]

    operations = [
        migrations.CreateModel(
            name='AnalysedScoresMaterializedView',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now_add=True)),
                ('score', models.FloatField()),
            ],
            options={
                'db_table': 'crypto_analysed_scores',
                'managed': False,
            },
        ),
        migrations.AlterModelOptions(
            name='analysedscores',
            options={},
        ),
    ]