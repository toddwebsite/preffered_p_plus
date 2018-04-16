from django.conf import settings

from django.conf.urls.static import static
from django.urls import include, path, re_path
from django.views.generic import TemplateView
from text.views import MainDetailView, MainView, SiteDataView
from listing.views import ListingHomeView

from django.contrib import admin


urlpatterns = [
    path("", ListingHomeView.as_view(template_name="homepage.html"), name="home"),
    path("staff_options/", TemplateView.as_view(template_name="staff_options.html"), name="staff_options"),
    # ath("", TemplateView.as_view(template_name="homepage.html"), name="home"),
    path("backend/", admin.site.urls),
    path("account/", include("account.urls")),
    path("listing/", include("listing.urls")),
    path("<slug:slug>/update/", SiteDataView.as_view(template_name="form.html"), name="site_data"),
    re_path(r"^ajax/images/", include("pinax.images.urls", namespace="pinax_images")),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
