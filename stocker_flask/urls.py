from config import app
import views as v
from flask import request

@app.route("/")
def index():
    print 'routed works'
    return v.index("static/index.html")

@app.route('/api/v1.0/defaultExcoList', methods=['GET'])
def get_default_exco_list():
    return v.getDefaultExcoList()

@app.route('/api/v1.0/portfolio', methods=['POST'])
def create_portfolio():
    return v.createPortfolio(request)

@app.route('/api/v1.0/portfolio/<portfolio_id>', methods=['GET'])
def get_portfolio(portfolio_id):
    return v.getPortfolio(portfolio_id)

@app.route('/api/v1.0/portfolio/<portfolio_id>/purchase', methods=['POST'])
def add_purchase(portfolio_id):
    return v.addPurchase(portfolio_id, request)

@app.route('/api/v1.0/portfolio/<portfolio_id>/purchases', methods=['GET'])
def get_purchases(portfolio_id):
    return v.getPurchases(portfolio_id)

@app.route('/api/v1.0/purchase/<purchase_id>', methods=['GET'])
def get_purchase(purchase_id):
    return v.getPurchase(purchase_id)