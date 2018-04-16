from django.db import models

from django.db.models.signals import pre_save
from django.urls import reverse
from django.utils.text import slugify
from django.utils.translation import ugettext_lazy as _

from listing.models import Listing

from versatileimagefield.fields import (
    VersatileImageField, 
    PPOIField
)


class Picture(models.Model):
    slug = models.SlugField(max_length=150, blank=True)
    origin = models.DateTimeField(auto_now_add=True, null=True)
    listing = models.ForeignKey(Listing, related_name="listing", verbose_name=_("listing"), on_delete=models.CASCADE)
    caption = models.CharField(_('caption'), max_length=70, null=True, blank=True)
    detail_image = VersatileImageField(
        'Detail Image',
        upload_to='images/detail_listing/',
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

    def __str__(self):
        return self.detail_image