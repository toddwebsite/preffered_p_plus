from django.urls import path, re_path

from .views import (
    ListingDetailView,
    ListingView,
    ListingCreate,
    ListingUpdate
    )


app_name = 'listing'
urlpatterns = [  
    re_path(r'^listing/(?P<slug>[-\w]+)/detail/$', ListingDetailView.as_view(),
        name="listing_detail"),
    re_path(r'^properties/$', ListingView.as_view(),
        name="listing_list"),
    re_path(r'^create/(?P<arg>[-\w]+)/$', ListingCreate.as_view(),
        name="listing_create"),
    re_path(r'^(?P<slug>[-\w]+)/update/$', ListingUpdate.as_view(),
        name="listing_update"),
]