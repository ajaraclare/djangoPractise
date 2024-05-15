from django.urls import path
from.import views

app_name= 'members'

urlpatterns = [
    path('', views.member, name="member"),
    path('about/', views.about, name="about"),
    path('contact/', views.contact, name="contact")
]