from django.shortcuts import render, get_object_or_404, redirect

from .models import Article, Comment

# Create your views here.

"""
actions about model Article
"""


def article_list(request):
    articles = Article.objects.all()
    return render(request, 'simple_board/list.html', {'articles': articles})


def article_create(request):
    if request.method == 'GET':
        return render(request, 'simple_board/create.html')
    else:
        article = Article()
        article.title = request.POST.get('title')
        article.content = request.POST.get('content')
        article.save()
        return redirect('simple_board:article_detail', article.id)


def article_detail(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    context = {
        'article': article,
        'comments': article.comment_set.all()
    }
    return render(request, 'simple_board/detail.html', context)


def article_update(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    if request.method == 'GET':
        return render(request, 'simple_board/update.html', {'article': article})
    else:
        article.title = request.POST.get('title')
        article.content = request.POST.get('content')
        article.save()
    return redirect('simple_board:article_detail', article_id)


def article_delete(request, article_id):
    if request.method == 'GET':
        return redirect('simple_board:article_detail', article_id)
    else:
        article = get_object_or_404(Article, id=article_id)
        article.delete()
        return redirect('simple_board:article_list')


"""
actions about model Comment
"""


def comment_create(request, article_id):
    if request.method == 'POST':
        comment = Comment()
        comment.content = request.POST.get('content')
        comment.article = get_object_or_404(Article, id=article_id)
        comment.save()
    return redirect('simple_board:article_detail', article_id)


def comment_delete(request, article_id, comment_id):
    if request.method == 'POST':
        comment = Comment.objects.get(id=comment_id)
        comment.delete()
    return redirect('simple_board:article_detail', article_id)
