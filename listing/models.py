from django.db import models

from django.db.models.signals import pre_save
from django.urls import reverse
from django.utils.text import slugify
from django.utils.translation import ugettext_lazy as _


from account.models import Account
from versatileimagefield.fields import (
    VersatileImageField, 
    PPOIField
)

ROOM_OPTION = (
        ('NA', 'Not Applicable'),
        ('0', '0'),
        ('1', '1'),
        ('1.5', '1.5'),
        ('2', '2'),
        ('2.5', '2.5'),
        ('3', '3'),
        ('3.5', '3.5'),
        ('4', '4'),
        ('4.5', '4.5'),
        ('5', '5'),
        ('5.5', '5.5'),
        ('6', '6'),
        ('6.5', '6.5'),
        ('7+', '7+'),
    )


class Listing(models.Model):
    slug = models.SlugField(max_length=150, blank=True)
    origin = models.DateTimeField(auto_now_add=True, null=True)
    last_modified = models.DateTimeField(auto_now=True, null=True)
    agent = models.ForeignKey(Account, related_name="agent", verbose_name=_("valued agent"), on_delete=models.CASCADE)
    name = models.CharField(_('property name'), max_length=30)
    street = models.CharField(_('street address'), max_length=150)
    city = models.CharField(_('city'), max_length=150)
    state = models.CharField(_('state'), max_length=150)
    zipcode = models.CharField(_('zipcode'), max_length=15)
    desription = models.TextField(_('description'), max_length=4000)
    county = models.CharField(_('county'), max_length=50)
    school_district = models.CharField(_('school district'), max_length=150)
    elementary_sch = models.CharField(_('elementary school'), max_length=150)
    middle_sch = models.CharField(_('middle school'), max_length=150)
    high_sch = models.CharField(_('high school'), max_length=150)
    available = models.BooleanField(
        _('available'),
        default=True,
    )
    sold = models.BooleanField(
        _('sold'),
        default=False,
    )
    image = VersatileImageField(
        'Main Image',
        upload_to='images/main_listing/',
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
    price_reduced = models.BooleanField(
        _('price reduced'),
        default=False,
    )
    motivated = models.BooleanField(
        _('motivated seller'),
        default=False,
    )
    price = models.PositiveIntegerField(
        _('listing price'),
        default=1
    )
    bedrooms = models.CharField(
        _('bedrooms'),
        max_length=15,
        choices=ROOM_OPTION,
        default='0',
    )
    bathrooms = models.CharField(
        _('bathrooms'),
        max_length=15,
        choices=ROOM_OPTION,
        default='0',
    )
    square_feet = models.PositiveIntegerField(
        _('square feet'),
        default=1
    )
    acres = models.DecimalField(
        _('acres'),
        max_digits=10,
        decimal_places=2,
        default=1
    )
    mls_number = models.PositiveIntegerField(
        _('MLS number'),
        default=1
    )
    built_in = models.PositiveSmallIntegerField(
        _('built in'),
        default=0
    )

    class Meta:
        verbose_name = _("Listing")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('listing:listing_detail',kwargs = {'slug' : self.slug})

    def get_address(self):
        return "{} {} {}".format(
                self.city,
                self.state,
                self.zipcode
                )

def pre_save_listing(sender, instance, *args, **kwargs):
    slug = "{} {} {} {}".format(
        instance.name,
        instance.street,
        instance.city,
        instance.pk
        )

    instance.slug = slugify(slug)

pre_save.connect(pre_save_listing, sender=Listing)
