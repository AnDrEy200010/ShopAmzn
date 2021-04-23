from django.conf.urls import url

from .views import product_list
from .views import search

app_name = 'products'

urlpatterns = [
    url(r'^$', product_list, name='product-list'),
    url(r'^search/$', search, name='search')
]
