from django.conf.urls import url
from . import views

urlpatterns = [

	url(r'^post_list/', 	views.PostListView.as_view(), name="post_list"),
	url(r'^$', 				views.MainPageView.as_view(), name="main_page"),
	url(r'^make_post/$', 	views.MakePostView.as_view(), name="make_post"),

]

