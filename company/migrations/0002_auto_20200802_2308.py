# Generated by Django 3.0.8 on 2020-08-03 02:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='cnpj',
            field=models.CharField(max_length=14, unique=True),
        ),
    ]
