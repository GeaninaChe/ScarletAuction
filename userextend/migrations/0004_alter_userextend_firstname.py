# Generated by Django 4.1.3 on 2022-11-03 18:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userextend', '0003_alter_userextend_firstname'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userextend',
            name='firstname',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
