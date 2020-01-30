from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='elo-home'),
    path('mlb/', views.mlb, name='elo-mlb'),
]
