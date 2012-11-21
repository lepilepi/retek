from django.conf.urls import patterns, include, url

from django.contrib import admin
from retek.views import order_food_service

admin.autodiscover()

urlpatterns = patterns('',

    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),

    url(r'^order/', order_food_service),

    url(r'^', include('restaurants.urls')),

)
