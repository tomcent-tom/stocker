# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Portfolio(models.Model):
    name = models.CharField(max_length=200)

class Purchase(models.Model):
    portfolio = models.ForeignKey(Portfolio, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    stock_id = models.CharField(max_length=5)
    volume = models.IntegerField(default=0)
    price = models.IntegerField(default=0)

