
#import Django function url and corresponding views from blog app
from django.conf.urls import url
from . import views

#regex: only match an empty string 
#name used to idenitfy the view
urlpatterns = [
	url(r'^$', views.post_list, name='post_list'),
]