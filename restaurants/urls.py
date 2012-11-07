from restaurants.views import RestaurantListView, CreateRestaurantView, CreateContractView, ContractListView
from django.views.generic.base import TemplateView
from django.conf.urls import patterns, url

urlpatterns = patterns('',
    url(r'^restaurants/new/$', CreateRestaurantView.as_view(), name='create_restaurant'),
    url(r'^restaurants/$', RestaurantListView.as_view(), name='restaurant_list'),

    url(r'^contracts/new/$', CreateContractView.as_view(), name='create_contract'),
    url(r'^contracts/$', ContractListView.as_view(), name='contract_list'),

    url(r'^$', TemplateView.as_view(template_name='index.html'), name='index'),

)
