from django.conf.urls import url
from . import views

urlpatterns = [

	url(r'^post_list/', views.post_list),
	url(r'^$', views.main_page),
# 7aea2a59a5c4b44f846eaae00e9ab60cfc7f07d6
]

