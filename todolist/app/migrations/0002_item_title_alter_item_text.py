# Generated by Django 5.0.3 on 2024-03-17 04:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='title',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='item',
            name='text',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
