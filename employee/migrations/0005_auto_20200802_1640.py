# Generated by Django 3.0.8 on 2020-08-02 19:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0004_auto_20200802_1638'),
    ]

    operations = [
        migrations.RenameField(
            model_name='employee',
            old_name='username_employee',
            new_name='nick_name',
        ),
    ]