# Generated by Django 4.1.6 on 2023-02-12 20:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0005_ticket_client_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticket',
            name='schedule_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='tickets.schedule'),
            preserve_default=False,
        ),
    ]