# Generated by Django 2.2.5 on 2019-09-06 08:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='specific',
            field=models.TextField(blank=True, max_length=6000, null=True, verbose_name='Описание'),
        ),
    ]
