# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.contrib import admin

from .models import Product, News


class ProductAdmin(admin.ModelAdmin):
    list_display = ['data']
    search_fields = ['data']


admin.site.register(Product,ProductAdmin)
admin.site.register(News)