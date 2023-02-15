# Generated by Django 4.1.6 on 2023-02-12 19:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0023_alter_herafiinformation_requests_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='herafiinformation',
            name='experiences',
            field=models.DecimalField(decimal_places=1, default=0, max_digits=3),
        ),
        migrations.AlterField(
            model_name='herafiinformation',
            name='price_of_preview',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=5),
        ),
        migrations.AlterField(
            model_name='herafiinformation',
            name='requests',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='herafiinformation',
            name='views',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]