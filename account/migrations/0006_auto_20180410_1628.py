# Generated by Django 2.0.4 on 2018-04-10 16:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0005_auto_20180410_1458'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='last_modified',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AddField(
            model_name='account',
            name='origin',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='account',
            name='slug',
            field=models.SlugField(blank=True, max_length=150),
        ),
    ]