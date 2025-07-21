from django.urls import path
from . import views

from django.views.defaults import page_not_found

urlpatterns = [
    path('', views.index, name='index'),
    path('.well-known/appspecific/com.chrome.devtools.json' , page_not_found, {'exception': None}),
]