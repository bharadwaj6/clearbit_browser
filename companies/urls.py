from django.conf.urls import url

from .views import CompanyAddedView, CompanySearchView

urlpatterns = [
    url(r'^$', CompanyAddedView.as_view(), name='company_list'),
    url(r'^search/$', CompanySearchView.as_view(), name='company_search'),
]
