from django.conf.urls import url

from .views import product_list
from .views import search
from .views import downfile

app_name = 'products'

urlpatterns = [
    url(r'^$', product_list, name='product-list'),
    url(r'^search/$', search, name='search'),
    url(r'^downfile/$', downfile, name='downfile'),
]
