from django.http import HttpResponse
from django.shortcuts import render

from .fakeDB import articles

def contact_view(request):
    return render(request, 'contact.html')

def home_view(request):
    return render(request, 'home.html')

def article_view(request):
    return render(request, 'article.html', context={'articles': articles})