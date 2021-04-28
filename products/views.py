from __future__ import unicode_literals
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from shopping_cart.models import Order
from .models import Product, News
from django.db.models import Q
from django.http import HttpResponseRedirect
import xml.etree.ElementTree as ET



@login_required
def product_list(request):
    object_list = Product.objects.all()
    filtered_orders = Order.objects.filter(owner=request.user.profile, is_ordered=False)
    current_order_products = []
    news_list = News.objects.filter().order_by('-date')[:3]

    if filtered_orders.exists():
    	user_order = filtered_orders[0]
    	user_order_items = user_order.items.all()
    	current_order_products = [product.product for product in user_order_items]

    context = {
        'object_list': object_list,
        'current_order_products': current_order_products,
        'news_list': news_list,
    }

    return render(request, "products/product_list.html", context)


@login_required
def search(request):
    query = request.POST['search']
    result_list = Product.objects.filter(Q(city__contains=query) | Q(state__contains=query))
    filtered_orders = Order.objects.filter(owner=request.user.profile, is_ordered=False)
    current_order_products = []
    if filtered_orders.exists():
        user_order = filtered_orders[0]
        user_order_items = user_order.items.all()
        current_order_products = [product.product for product in user_order_items]

    context = {
        'query': query,
        'result_list': result_list,
        'current_order_products': current_order_products
    }

    return render(request, 'products/search.html', context)


@login_required
def downfile(request):
    if not request.user.is_staff:
        return HttpResponseRedirect('/products/')
    if request.method == 'POST':
        upload = request.FILES['file']
        tree = ET.parse(upload)
        root = tree.getroot()
        for product in root:
            state = product.find('state').text
            city = product.find('city').text
            data = product.find('data').text
            status = product.find('status').text
            number_track = product.find('number_track').text
            price = product.find('price').text
            Product.objects.create(state=state, city=city, data=data, status=status, number_track=number_track, price=price)
        return HttpResponseRedirect('/admin/')
    else:
        context = {}
    return render(request, 'products/file.html', context)

