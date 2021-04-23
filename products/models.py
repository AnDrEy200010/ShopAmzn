# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Product(models.Model):
    state = models.CharField(max_length=50, verbose_name='Штат')
    city = models.CharField(max_length=50, verbose_name='Город')
    data = models.DateField(auto_now=False, verbose_name='Дата')
    status = models.CharField(max_length=50, verbose_name='Статус')
    number_track = models.CharField(max_length=50, verbose_name='Номер трека')
    price = models.IntegerField()

    def __str__(self):
        return self.number_track

