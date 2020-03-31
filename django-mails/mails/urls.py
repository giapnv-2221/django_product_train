from django.conf.urls import url
# from django.urls import path
from . import views

app_name = "mails"
urlpatterns = [
    url("^new/$", views.send_mail, name="new")
]
