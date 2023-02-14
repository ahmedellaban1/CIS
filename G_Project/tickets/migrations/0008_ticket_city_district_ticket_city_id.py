# Generated by Django 4.1.6 on 2023-02-12 20:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_info', '0007_alter_job_id'),
        ('tickets', '0007_ticket_job_category_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticket',
            name='city_district',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, to='main_info.citydistrict'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='ticket',
            name='city_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, to='main_info.city'),
            preserve_default=False,
        ),
    ]
