# Generated by Django 4.2 on 2024-07-21 08:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cards', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='card',
            name='tags',
            field=models.JSONField(default=list),
        ),
    ]