from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^(?P<p_id>[0-9]+)/$', views.getPortfolio, name='getPortfolio'),
]

