from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('trends/', views.trends, name='trends'),
    path('celebrity-style/', views.celebrity_style, name='celebrity_style'),
    path('street-style/', views.street_style, name='street_style'),
    path('beauty/', views.beauty, name='beauty'),
    path('picks/', views.picks, name='picks'),
]



