# Generated by Django 4.1.3 on 2022-11-22 18:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userextend', '0006_remove_userextend_account_userextend_is_buyer_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userextend',
            old_name='is_buyer',
            new_name='buyer',
        ),
        migrations.RenameField(
            model_name='userextend',
            old_name='is_seller',
            new_name='seller',
        ),
    ]
