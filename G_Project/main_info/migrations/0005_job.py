# Generated by Django 4.1.6 on 2023-02-12 18:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_info', '0004_alter_citydistrict_city'),
    ]

    operations = [
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=20)),
            ],
        ),
    ]