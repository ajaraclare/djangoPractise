from django.shortcuts import render
from.models import Info

# Create your views here.

def app2(request):
    return render(request, 'app2.html')

def input(request):
    if request.method == "POST":
        name = request.POST.get ('Name')
        email = request.POST.get ('Email')
        password = request.POST.get('password')

        data=Info(name=name, email=email, password=password)
        data.save()

    return render(request, 'app2.html')


