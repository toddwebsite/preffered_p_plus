from django.db import models

from django.db.models.signals import pre_save
from django.urls import reverse
from django.utils.text import slugify
from django.utils.translation import ugettext_lazy as _

from versatileimagefield.fields import (
    VersatileImageField, 
    PPOIField
)

COLOR_OPTION = (
        ('#4A4A4A', 'Black'),
        ('#F6F6F6', 'White'),
        ('#e3827b', 'Red'),
        ('#e3b67b', 'Tan'),
        ('#45a9ca', 'Blue'),
    )

class Details(models.Model):
    slug = models.SlugField(max_length=150, blank=True)
    origin = models.DateTimeField(auto_now_add=True, null=True)
    last_modified = models.DateTimeField(auto_now=True, null=True)
    caption = models.CharField(_('caption'), max_length=500, null=True, blank=True)
    bio = models.TextField(_('company bio'), max_length=4000, null=True, blank=True)
    alert = models.TextField(_('company alert'), max_length=4000, null=True, blank=True)
    image = VersatileImageField(
        'Site Image',
        null=True, blank=True,
        upload_to='images/site/',
        width_field='width',
        height_field='height'
    )
    height = models.PositiveIntegerField(
        'Image Height',
        blank=True,
        null=True
    )
    width = models.PositiveIntegerField(
        'Image Width',
        blank=True,
        null=True
    )
    ppoi = PPOIField(
        'Image PPOI'
    )
    phone_number = models.CharField(_('main phone'), max_length=12, blank=True)
    alt_phone_number = models.CharField(_('second phone'), max_length=12, null=True, blank=True)
    email = models.EmailField(_('company email address'), blank=True)
    text_color = models.CharField(_('text color'), max_length=30,
        choices=COLOR_OPTION,
        default='Black',
    )

    class Meta:
        verbose_name = _("Site detail")

    def __str__(self):
        return self.caption

    def get_absolute_url(self):
        return reverse('home', kwargs = {'slug' : 'home'})

def pre_save_site_details(sender, instance, *args, **kwargs):
    instance.slug = slugify("site_data")

pre_save.connect(pre_save_site_details, sender=Details)