# Generated by Django 4.1.6 on 2023-02-12 20:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('datetime', models.DateTimeField()),
                ('active', models.BooleanField(default=True)),
                ('evaluation', models.FloatField()),
                ('comment', models.TimeField(blank=True, max_length=1000, null=True)),
                ('status', models.CharField(choices=[('pending', 'pending'), ('done', 'done'), ('expired', 'expired'), ('been refused', 'been refused')], default=0, max_length=12)),
                ('description', models.TimeField(help_text='describe your problem ', max_length=2000)),
            ],
        ),
    ]
