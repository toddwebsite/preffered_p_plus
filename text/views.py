from django.shortcuts import render

from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView
from django.urls import reverse_lazy

from .models import Details
from .forms import SiteDataForm


class MainView(ListView):
    model = Details
    template_name = "homepage.html"

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['detail'] = get_object_or_404(Details, pk=1)
    #     print(context['detail'].image)
    #     return context


class MainDetailView(DetailView):
    model = Details
    template_name = "homepage.html"

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['detail'] = get_object_or_404(Details, pk=1)
    #     print(context['detail'].image)
    #     return context


class SiteDataView(UpdateView):
    model = Details
    fields = ['caption', 'bio', 'image', 'phone_number',
        'email', 'alt_phone_number', 'text_color',]
    template_name = "form.html"
    # form_class = SiteDataForm
    success_url = reverse_lazy('home')
    title = "Update Website Details"
    button = "Change"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = self.title
        context['button'] = self.button
        return context
