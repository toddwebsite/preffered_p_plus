from .views import (
    ListingDetailView,
    ListingView
    )


app_name = 'listing'
urlpatterns = [  
    re_path(r'^listing/(?P<slug>[-\w]+)/detail/$', ListingDetailView.as_view(),
        name="listing_detail"),
    re_path(r'^properties/$', ListingView.as_view(),
        name="listing_list"),
    # url(r'^payroll/(?P<pk>\d+)/update/$', PayRollStaffUpdate.as_view(),
    #     name="payroll_update"),
    # url(r'^staff/(?P<pk>\d+)/payroll_detail/$', PayRollDetail.as_view(),
    #     name="staff_payroll_detail"),

    # url(r'^benefit/create/$', BenefitCreate.as_view(),
    #     name="benefit_create"),
    # url(r'^benefit/(?P<pk>\d+)/update/$', BenefitUpdate.as_view(),
    #     name="benefit_update"),
    # url(r'^benefit_list/$', BenefitList.as_view(), 
    #     name="benefit_list"),

    # url(r'^single_tax_bracket/(?P<pk>\d+)/update/$', 
    #     SinglePersonTaxBracketsUpdate.as_view(),
    #     name="single_tax_bracket_update"),
    # url(r'^married_tax_bracket/(?P<pk>\d+)/update/$', 
    #     MarriedPersonTaxBracketsUpdate.as_view(),
    #     name="married_tax_bracket_update"),
    # url(r'^dependent_deduction/(?P<pk>\d+)/update/$', 
    #     PreTaxDeductionUpdate.as_view(),
    #     name="dependent_deduction"),
    # url(r'^medicare_social_security/(?P<pk>\d+)/update/$', 
    #     MedicareAndSocialSecurityUpdate.as_view(),
    #     name="medicare_social_security"),
]