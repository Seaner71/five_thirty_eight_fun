# Generated by Django 3.0.2 on 2020-02-17 02:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('elo', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='conference',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='team',
            name='division',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='team',
            name='league',
            field=models.CharField(max_length=5, null=True),
        ),
    ]
