from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from article.models import Article


def list_view(request):
    articles = Article.objects.all()
    return render(request, 'articles/list.html', context={'articles': articles})

def detail_view(request, id):
    article = get_object_or_404(Article, id=id)
    return render(request, 'articles/detail.html', context={'article': article})