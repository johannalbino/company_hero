# Generated by Django 3.0.8 on 2020-08-03 13:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Log',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key', models.CharField(max_length=255, verbose_name='Identificador da requisição')),
                ('value', models.TextField(verbose_name='Dados da requisição/resposta')),
            ],
            options={
                'verbose_name': 'Log',
                'verbose_name_plural': 'Logs',
                'db_table': 'company_hero_log',
            },
        ),
    ]
