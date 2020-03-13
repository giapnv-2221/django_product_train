from django.conf.urls import url
from . import views

app_name = "contact"
urlpatterns = [
    url('^sendmail/$', views.ContactView.as_view(), name='sendmail'),

]
