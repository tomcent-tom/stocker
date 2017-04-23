# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
import requests
from django.shortcuts import render
from . import models
from . import config
import json
import datetime

def index(request):
    return HttpResponse("Hello, world. Tom houdt van Tis.")
# Create your views here.

def getStockRate(request, stock_id):
    stock = config.Bel20[stock_id]
    response = requests.get(config.Bloomber_url+stock['ref'])
    joutput = json.loads(response.content)
    return HttpResponse(joutput['price'])

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

def getExcoList(request, date1, date2):
    if date2 is None:
        end_date = datetime.date.today()
    else:
        end_date = datetime.strptime(date2, '%d-%m-%Y')
    start_date = datetime.strptime(date1, '%d-%m-%Y')

def getDefaultExcoList(request):
    url = config.fsma_url['baseline_default']
    response = requests.get(url)
    data = config.convert_html_to_matrix(response.content)
    j_data = config.convert_matrix_to_table(data)
    for purchase in j_data:
        url = config.fsma_url['baseline_extra']+purchase['Href']
        response = requests.get(url)
        extra_data = config.get_extra_exco_data(response.content)
        purchase.update(extra_data)
    return HttpResponse(json.dumps(j_data))