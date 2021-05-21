from django.conf.urls import url

from .views import my_profile
from .views import copy_from_cart

app_name = 'accounts'

urlpatterns = [
	url(r'^profile/$', my_profile, name='my_profile'),
	url(r'^item/copy/(?P<item_id>[-\w]+)/$', copy_from_cart, name='copy_item'),


]

