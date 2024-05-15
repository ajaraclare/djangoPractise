from django.shortcuts import render, HttpResponse

# Create your views here.
def member(request):
    return render(request, 'myfirst/myfirst.html')

def about(request):
    return render(request, 'about/about.html')

def contact(request):
    return render(request, 'contact/contact.html')