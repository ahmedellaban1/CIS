# Generated by Django 4.1.6 on 2023-02-12 18:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_info', '0005_job'),
    ]

    operations = [
        migrations.AlterField(
            model_name='city',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]