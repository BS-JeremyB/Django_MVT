from django.shortcuts import render
from django.http import HttpResponse

from .fakeDB import articles
# Create your views here.

def list_view(request):
    return render(request, 'articles/list.html', context={'articles': articles})


def detail_view(request, id):
    article = next((article for article in articles if article['id'] == id), None)
    if article:
        return render(request, 'articles/detail.html', context={'article': article})
    else:
        # Handle case where article with given id does not exist
        return HttpResponse(f"il n'y a pas d'article à l'id {id}")