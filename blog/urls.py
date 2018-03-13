from django.conf.urls import url
from . import views

urlpatterns = [
 url(r'^add/blog/$', views.add_blog , name='add_blog'),
]