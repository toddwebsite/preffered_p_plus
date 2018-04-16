# Generated by Django 2.0.4 on 2018-04-13 00:44

from django.db import migrations, models
import versatileimagefield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('text', '0005_details_text_color'),
    ]

    operations = [
        migrations.AddField(
            model_name='details',
            name='height',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name='Image Height'),
        ),
        migrations.AddField(
            model_name='details',
            name='ppoi',
            field=versatileimagefield.fields.PPOIField(default='0.5x0.5', editable=False, max_length=20, verbose_name='Image PPOI'),
        ),
        migrations.AddField(
            model_name='details',
            name='width',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name='Image Width'),
        ),
        migrations.AlterField(
            model_name='details',
            name='image',
            field=versatileimagefield.fields.VersatileImageField(blank=True, height_field='height', null=True, upload_to='images/main_listing/', verbose_name='Site Image', width_field='width'),
        ),
    ]