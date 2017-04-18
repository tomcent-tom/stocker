# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.shortcuts import render
from . import models
import json

def index(request):
    return HttpResponse("Hello, world. Tom houdt van Tis.")
# Create your views here.

def getStockRate(request):

    return HttpResponse("10,20,30,40")

def getPortfolio(request, p_id):
    p = models.Portfolio.objects.get(id=p_id)
    purchases = p.purchase_set.all()
    response = {}
    response['id'] = p_id
    response['name'] = p.name
    pcs_json = []
    for purchase in purchases:
        temp = {}
        temp['name']=purchase.name
        temp['stock_id'] = purchase.stock_id
        temp['volume'] = purchase.volume
        temp['price'] = purchase.price
        pcs_json.append(temp)
    response['purchases'] = pcs_json
    return HttpResponse(json.dumps(response))

