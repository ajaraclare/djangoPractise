from django.shortcuts import render, HttpResponse

# Create your views here.
def member(request):
    return render(request, 'myfirst.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')