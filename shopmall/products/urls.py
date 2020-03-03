from django.conf.urls import url, include
# from django.urls import path
from . import views
app_name = "products"
urlpatterns = [
    url('^$', views.index, name='index'),
    url('^(?P<product_id>[0-9]+)/$', views.show, name='show'),
    url(r'^new/$', views.new, name='new'),
    # url('/', views.create, name='create'),
    url(r'^edit/(?P<product_id>[0-9]+)/$', views.edit, name='edit'),
    url(r'^<int:id>/$', views.update, name='update'),
    url(r'^<int:id>/$', views.destroy, name='destroy'),
]
