# Generated by Django 4.1.6 on 2023-02-12 14:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_alter_profile_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='banned',
            field=models.BooleanField(default=False),
        ),
    ]