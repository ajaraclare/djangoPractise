from django.urls import path, include
from.import views


urlpatterns = [
    path('', views.app2, name="app2"),
    path('firstapp/', include("members.urls")),
    path('input/', views.input, name="input")
]