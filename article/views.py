from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse


from article.models import Article
from .forms import ArticleForm


def list_view(request):
    articles = Article.objects.all()
    return render(request, 'articles/list.html', context={'articles': articles})

def detail_view(request, id):
    article = get_object_or_404(Article, id=id)
    return render(request, 'articles/detail.html', context={'article': article})

def create_view(request):
    form = ArticleForm()
    if(request.method == "POST"):
        form = ArticleForm(request.POST)
        if(form.is_valid()):
            form.save()
            return redirect('article:articles')
    return render(request, 'articles/create.html', context={'form': form})