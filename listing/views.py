from django.shortcuts import get_object_or_404, redirect, render

from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView
# from myapp.models import Author

from .models import Listing
from .forms import ListingCreateForm
from text.models import Details
from picture.models import Picture


class ListingCreate(CreateView):
    model = Listing
    title = "Create New Listing"
    button = "Add Listing"
    # fields = ['image', 'price', 'bedrooms', 'bathrooms', 'square_feet', 'acres',
    #     'mls_number', 'built_in', 'agent', 'name', 'street', 'city', 'state', 'zipcode', 'county',
    #     'desription', 'school_district', 'elementary_sch', 'middle_sch',
    #     'high_sch', 'available', 'sold', 'price_reduced', 'motivated']
    template_name = "form.html"
    form_class = ListingCreateForm

    # def get_form(self, form_class):
    #     form = super(ListingCreate, self).get_form(form_class)
    #     form.fields['agent'] = self.request.user #self.kwargs['arg']
    #     return form

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = self.title
        context['button'] = self.button
        return context

    

    def get_initial(self):
        initial = super(ListingCreate, self).get_initial()
        agent = self.kwargs['arg']
        print(self.kwargs['arg'])
        initial["agent"] = self.request.user
        return initial
        return {
            'agent':agent,
            'price':2333
        }


class ListingUpdate(UpdateView):
    model = Listing
    title = "Update New Listing"
    button = "Update"
    fields = ['image', 'price', 'bedrooms', 'bathrooms', 'square_feet', 'acres',
        'mls_number', 'built_in', 'agent', 'name', 'street', 'city', 'state', 'zipcode', 'county',
        'desription', 'school_district', 'elementary_sch', 'middle_sch',
        'high_sch', 'available', 'sold', 'price_reduced', 'motivated']
    template_name = "form.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = self.title
        context['button'] = self.button
        return context


class ListingHomeView(ListView):
    model = Listing
    template_name = "homepage.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['detail'] = get_object_or_404(Details, pk=1)
        return context


class ListingView(ListView):
    model = Listing
    template_name = "listings.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['detail'] = get_object_or_404(Details, pk=1)
        return context


class ListingDetailView(DetailView):
    model = Listing
    context_object_name = 'listing'
    template_name = "listing_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['detail'] = get_object_or_404(Details, pk=1)
        print(self.object.name)
        context['pic_list'] = Picture.objects.filter(listing=self.object)
        return context


    # def get_context_data(self, **kwargs):
    #     context = super(ListingDetailView, self).get_context_data(**kwargs)
    #     context['now'] = timezone.now()
    #     context['detail'] = get_object_or_404(Details, pk=1)
    #     context['trial'] = "trial"
    #     print(context['detail'])
    #     return context

    # def get_context_data(self, **kwargs):
    #     context = super(MainLedgerDetailView, self).get_context_data(**kwargs)
    #     #get customer financial details
    #     (
    #         total, 
    #         taxes,
    #         profit, 
    #         customers_balances, 
    #         customers_count, 
    #         customers_conflicts, 
    #         customers_unresolved_conflicts,
    #         projected_before_tax
    #     ) = self.object.get_customer_balance_sheet()

    #     context['customers_total'] = total
    #     context['customers_taxes'] = taxes
    #     context['customers_profit'] = profit
    #     context['customers_balances'] = customers_balances
    #     context['customers_count'] = customers_count
    #     context['customers_conflicts'] = customers_conflicts
    #     context['customers_unresolved_conflicts'] = customers_unresolved_conflicts
    #     context['projected_before_tax'] = projected_before_tax
    #     #get operational expenses
    #     (
    #         expenses, 
    #         operation_balances, 
    #         operation_count, 
    #         operation_conflicts, 
    #         operation_unresolved_conflicts
    #     ) = self.object.get_operation_balance_sheet()
    #     context['operation_expenses'] = expenses
    #     context['operation_balances'] = operation_balances
    #     context['operation_count'] = operation_count
    #     context['operation_conflicts'] = operation_conflicts
    #     context['operation_unresolved_conflicts'] = operation_unresolved_conflicts
    #     context['net_profit'] = profit - expenses
    #     context['get_payrole_balance_sheet'] = self.object.get_payrole_balance_sheet()


    #     return context
