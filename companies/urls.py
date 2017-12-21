from django.conf.urls import url

from .views import CompanyAddedView, CompanySearchView, CompanyDeleteView

urlpatterns = [
    url(r'^$', CompanyAddedView.as_view(), name='company_list'),
    url(r'^search/$', CompanySearchView.as_view(), name='company_search'),
    url(r'^delete/(?P<pk>\d+)$', CompanyDeleteView.as_view(), name='company_delete'),
]
