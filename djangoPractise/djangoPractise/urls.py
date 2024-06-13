from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("members.urls")),
    path('app2/', include("APP2.urls")),
    path('w3schools/', include("w3schools.urls"))  
]
