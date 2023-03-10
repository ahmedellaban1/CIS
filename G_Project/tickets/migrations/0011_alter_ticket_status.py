# Generated by Django 4.1.6 on 2023-03-02 16:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0010_alter_ticket_evaluation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='status',
            field=models.CharField(choices=[('pending', 'pending'), ('done', 'done'), ('expired', 'expired'), ('been refused', 'been refused'), ('been accepted', 'been accepted')], default=0, max_length=13),
        ),
    ]
