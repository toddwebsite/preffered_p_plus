# Generated by Django 2.0.4 on 2018-04-12 14:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0006_auto_20180410_1628'),
        ('listing', '0005_listing_ppoi'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='agent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='agent', to='account.Account', verbose_name='valued agent'),
        ),
    ]
