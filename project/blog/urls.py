from django.conf.urls import url
from . import views

urlpatterns = [

	url(r'^post_list/', views.post_list, name="post_list"),
	url(r'^$', views.main_page, name="main_page"),
	url(r'^home/$', views.home, name="home"),

]

