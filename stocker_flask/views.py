# -*- coding: utf-8 -*-
from flask import Flask, send_file, request
import config
import json
import models
from config import db

def index(url):
    return send_file(url)

"""
def getStockRate(request, stock_id):
    stock = config.Bel20[stock_id]
    response = requests.get(config.Bloomber_url+stock['ref'])
    joutput = json.loads(response.content)
    return HttpResponse(joutput['price'])
"""

def getPortfolio(p_id):
    p = models.Portfolio.query.get(p_id)
    ##purchases = p.purchase_set.all()
    response = {}
    response['id'] = p_id
    response['name'] = p.username
    response['email'] = p.email
    """
    pcs_json = []
    for purchase in purchases:
        temp = {}
        temp['name']=purchase.name
        temp['stock_id'] = purchase.stock_id
        temp['volume'] = purchase.volume
        temp['price'] = purchase.price
        pcs_json.append(temp)
    response['purchases'] = pcs_json
    """
    response = json.dumps(response)
    return response


def createPortfolio(request):
    data = request.get_json()[0]
    portfolio = models.Portfolio(data['name'],data['email'])
    db.session.add(portfolio)
    db.session.commit()
    return str(portfolio.id)


def addPurchase(portfolio_id, request):
    data = request.get_json()[0]
    purchase = models.Purchase(data['name'],data['stock_id'],data['volume'],data['price'],portfolio_id)
    db.session.add(purchase)
    db.session.commit()
    return str(purchase.id)

def getPurchases(p_id):
    portfolio = models.Portfolio.query.get(p_id)
    purchases = []
    for purchase in portfolio.purchases:
        dic = purchase.__dict__
        dic.pop('_sa_instance_state', None)
        dic.pop('portfolio', None)
        dic.pop('portfolio_id', None)
        dic['volume'] = str(dic['volume'])
        dic['id'] = str(dic['id'])
        purchases.append(dic)
    response = json.dumps(purchases)
    return response

def getPurchase(p_id):
    purchase = models.Purchase.query.get(p_id)
    response = {}
    response['name'] = purchase.name
    response['id'] = str(purchase.id)
    response['stock_id'] = str(purchase.stock_id)
    response['volume'] = str(purchase.volume)
    response['price'] = str(purchase.price)
    response = json.dumps(response)
    return response
"""
def getExcoList(request, date1, date2):
    if date2 is None:
        end_date = datetime.date.today()
    else:
        end_date = datetime.strptime(date2, '%d-%m-%Y')
    start_date = datetime.strptime(date1, '%d-%m-%Y')
"""

def getDefaultExcoList():
    url = config.fsma_url['baseline_default']
    response = requests.get(url)
    data = config.convert_html_to_matrix(response.content)
    j_data = config.convert_matrix_to_table(data)
    for purchase in j_data:
        url = config.fsma_url['baseline_extra']+purchase['Href']
        response = requests.get(url)
        extra_data = config.get_extra_exco_data(response.content)
        purchase.update(extra_data)
    response = json.dumps(j_data)
    return response
