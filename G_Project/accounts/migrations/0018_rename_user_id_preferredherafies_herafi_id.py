# Generated by Django 4.1.6 on 2023-02-12 15:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0017_alter_preferredherafies_user_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='preferredherafies',
            old_name='user_id',
            new_name='herafi_id',
        ),
    ]
