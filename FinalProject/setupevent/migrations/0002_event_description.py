# Generated by Django 4.1.2 on 2022-11-16 13:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('setupevent', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='description',
            field=models.TextField(default='not defined yet'),
            preserve_default=False,
        ),
    ]
