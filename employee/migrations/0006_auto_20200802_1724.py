# Generated by Django 3.0.8 on 2020-08-02 20:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0005_auto_20200802_1640'),
    ]

    operations = [
        migrations.RenameField(
            model_name='employee',
            old_name='nick_name',
            new_name='username',
        ),
    ]