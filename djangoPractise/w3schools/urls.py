from django.urls import path
from.import views



urlpatterns = [
    path('', views.w3schools, name="table"),
    path('webpage/', views.webpage, name="webpage")
]