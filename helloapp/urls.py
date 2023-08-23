from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('helloapp', views.helloapp, name='helloapp'),
    path('helloapp/details/<int:id>', views.details, name='details'),
    path('testing/', views.testing, name='testing'),
]