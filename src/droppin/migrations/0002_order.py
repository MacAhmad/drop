# Generated by Django 4.2.6 on 2023-11-29 08:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('droppin', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cli_name', models.CharField(max_length=200, null=True)),
                ('cli_email', models.CharField(max_length=200, null=True)),
                ('cli_address', models.CharField(max_length=200, null=True)),
                ('cli_city', models.CharField(max_length=200, null=True)),
                ('cli_phone', models.CharField(max_length=200, null=True)),
                ('cli_subj', models.CharField(max_length=200, null=True)),
                ('cli_qty', models.CharField(max_length=200, null=True)),
                ('cli_date', models.DateTimeField(max_length=200, null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
            ],
            options={
                'ordering': ['-date_created'],
            },
        ),
    ]
