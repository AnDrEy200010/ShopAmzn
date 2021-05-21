from django.shortcuts import render, redirect, get_object_or_404
from shopping_cart.models import OrderItem
from shopping_cart.models import Order
from .models import Profile
from django.urls import reverse
import pyperclip
import subprocess
import pandas


def my_profile(request):
	my_user_profile = Profile.objects.filter(user=request.user).first()
	my_orders = Order.objects.filter(is_ordered=True, owner=my_user_profile)
	context = {
		'my_orders': my_orders
	}

	return render(request, "profile.html", context)


def copy_from_cart(request, item_id):
	item_to_copy = OrderItem.objects.filter(pk=item_id)
	if item_to_copy.exists():
		# pyperclip.copy(str(item_to_copy[0].product.number_track))
		df = pandas.DataFrame([str(item_to_copy[0].product.number_track)])
		df.to_clipboard(index=False, header=False)
	return redirect(reverse('accounts:my_profile'))