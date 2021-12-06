from django.urls import path, include
from pars.views import PostList
from django.conf.urls import url
urlpatterns = [
    
    path('', PostList.as_view(), name='index'),
    
]
