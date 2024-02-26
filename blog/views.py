from django.http import HttpResponse
from django.shortcuts import render


def contact_view(request):
    return render(request, 'contact.html')

def home_view(request):
    return render(request, 'home.html')
