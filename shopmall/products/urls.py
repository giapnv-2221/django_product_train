from django.conf.urls import url, include
# from django.urls import path
from . import views
app_name = "products"
urlpatterns = [
    url('^$', views.index, name='index'),
    url('^(?P<product_id>[0-9]+)/$', views.show, name='show'),
    url('^create/$', views.create, name='create'),
    url('^(?P<product_id>[0-9]+)/update/$', views.update, name='update'),
    url('^(?P<product_id>[0-9]+)/destroy/$', views.destroy, name='destroy'),
    url('^category/new$', views.CategoryCreateView.as_view(), name='category'),
    url('^category/(?P<pk>[0-9]+)/update', views.CategoryUpdateView.as_view(), name='update_category'),
]
