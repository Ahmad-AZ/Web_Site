from django.urls import path
from django.conf.urls import url
from . import views


urlpatterns = [
    # /music/
   # url path, the response ,
    path('', views.index , name='index'), # all url for the music file

    # /music/21/
    url(r'^(?P<album_id>[0-9]+)/$',views.detail,name='detail'),
]
