from __future__ import unicode_literals
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from shopping_cart.models import Order
from .models import Product, News
from django.db.models import Q
from django.http import HttpResponseRedirect
import xml.etree.ElementTree as ET
import csv
import io


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
    country = request.POST['country']
    state = request.POST['state']
    city = request.POST['city']
    result_list = Product.objects.filter(country__contains=country, state__contains=state, city__contains=city)
    filtered_orders = Order.objects.filter(owner=request.user.profile, is_ordered=False)
    current_order_products = []
    if filtered_orders.exists():
        user_order = filtered_orders[0]
        user_order_items = user_order.items.all()
        current_order_products = [product.product for product in user_order_items]

    context = {
        'country': country,
        'state': state,
        'city': city,
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
        data_set = upload.read().decode('UTF-8')
        io_string = io.StringIO(data_set)
        next(io_string)
        for column in csv.reader(io_string, delimiter=',', quotechar="|"):
            try:
                _, created = Product.objects.update_or_create(
                    country=column[0],
                    state=column[1],
                    city=column[2],
                    data=column[3],
                    status=column[4],
                    number_track=column[5],
                    price=column[6]
                )
            except Exception:
                continue

        # with open(os.path.abspath(upload.name), newline='') as f:
        #     reader = csv.reader(f)
        #     for row in reader:
        #         array = row.split(',')
        #         state = array[0].text
        #         city = array[1].text
        #         data = array[3].text
        #         status = array[4].text
        #         number_track = array[2].text
        #         price = array[5].text
        #         Product.objects.create(state=state, city=city, data=data, status=status, number_track=number_track, price=price)
        return HttpResponseRedirect('/admin/')
    else:
        context = {}
    return render(request, 'products/file.html', context)

