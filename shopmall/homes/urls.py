from django.conf.urls import url
from django.contrib.auth import views as auth_views
from . import views

app_name = "homes"
urlpatterns = [
    url('^$', views.index, name='index'),
    url('^login/$', auth_views.LoginView.as_view(template_name='homes/login.html'), name='login'),
    url('^logout/$', auth_views.LogoutView.as_view(next_page='/'), name='logout'),
    url('^register/$', views.register, name='register'),
]
