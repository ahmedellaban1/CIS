# Generated by Django 4.1.6 on 2023-03-03 20:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0012_alter_ticket_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ticket',
            name='schedule_id',
        ),
    ]
