from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('location/<int:location_id>', views.location, name='location'),
    path('help', views.howtohelp, name='howtohelp'),
    path('predict', views.predict, name='predict'),
    path('send/<int:location_id>', views.send, name='send')
]