from django.shortcuts import render

from .fakeDB import articles
# Create your views here.

def list_view(request):
    return render(request, 'articles/list.html', context={'articles': articles})