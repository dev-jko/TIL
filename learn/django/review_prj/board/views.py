from django.shortcuts import render, redirect
from .models import Article


# Create your views here.


def index(request):
    return render(request, 'board/index.html')


def greeting(request, name, role):
    if role == 'admin':
        role = 'MASTER USER'
    return render(request, 'board/greeting.html', {'name': name, 'role': role})


def article_new(request):
    return render(request, 'board/article_new.html')


def article_create(request):
    article = Article()
    article.title = request.POST.get('title')
    article.content = request.POST.get('content')
    article.save()
    return redirect(f'/board/articles/{article.id}')


def article_list(request):
    content = {'articles': Article.objects.all()}
    return render(request, 'board/article_list.html', content)


def article_detail(request, id):
    content = {'article': Article.objects.get(id=id)}
    return render(request, 'board/article_detail.html', content)


def article_edit(request, id):
    content = {'article': Article.objects.get(id=id)}
    return render(request, 'board/article_edit.html', content)


def article_update(request, id):
    article = Article.objects.get(id=id)
    article.title = request.POST.get('title')
    article.content = request.POST.get('content')
    article.save()
    return redirect(f'/board/articles/{article.id}')


def article_delete(request, id):
    article = Article.objects.get(id=id)
    article.delete()
    return redirect('/board/articles/')
