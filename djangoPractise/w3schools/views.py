from django.shortcuts import render, HttpResponse

# Create your views here.

def w3schools(request):
    return HttpResponse("w3schools")

def webpage(request):
    return render(request, 'schools.html')