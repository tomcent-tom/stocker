from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^portfolio/(?P<p_id>[0-9]+)/$', views.getPortfolio, name='getPortfolio'),
    url(r'^stock/(?P<stock_id>[A-z]+)/$', views.getStockRate, name='getStockRate'),
    url(r'^defaultExcoList/$', views.getDefaultExcoList, name='getDefaultExcoList'),
]

