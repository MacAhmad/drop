# Generated by Django 4.2.6 on 2023-11-29 09:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('droppin', '0002_order'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contactor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email_contactor', models.CharField(max_length=200, null=True)),
                ('mess_contactor', models.CharField(max_length=300, null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
            ],
            options={
                'ordering': ['-date_created'],
            },
        ),
    ]
