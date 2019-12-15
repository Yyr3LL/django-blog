from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls, name="admin_page"),
    url(r'', include('blog.urls')),
]
