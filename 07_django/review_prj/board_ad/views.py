from django.shortcuts import render, redirect, get_object_or_404
from .models import Posting, Comment
from django.views.decorators.http import require_http_methods


@require_http_methods(['GET'])
def posting_list(request):
    content = {'postings': Posting.objects.all()}
    return render(request, 'board_ad/posting_list.html', content)


@require_http_methods(['GET'])
def posting_detail(request, posting_id):
    posting = get_object_or_404(Posting, id=posting_id)
    content = {
        'posting': posting,
        'comments': posting.comment_set.all()
    }
    return render(request, 'board_ad/posting_detail.html', content)


@require_http_methods(['GET', 'POST'])
def posting_create(request):
    if request.method == 'POST':
        posting = Posting()
        posting.title = request.POST.get('title')
        posting.content = request.POST.get('content')
        posting.save()
        return redirect('board_ad:posting_detail', posting.id)
    else:
        return render(request, 'board_ad/posting_create.html')


@require_http_methods(['GET', 'POST'])
def posting_update(request, posting_id):
    if request.method == 'POST':
        posting = get_object_or_404(Posting, id=posting_id)
        posting.title = request.POST.get('title')
        posting.content = request.POST.get('content')
        posting.save()
        return redirect('board_ad:posting_detail', posting_id)
    else:
        content = {'posting': get_object_or_404(Posting, id=posting_id)}
        return render(request, 'board_ad/posting_update.html', content)


@require_http_methods(['POST'])
def posting_delete(request, posting_id):
    posting = get_object_or_404(Posting, id=posting_id)
    posting.delete()
    return redirect('board_ad:posting_list')


@require_http_methods(['POST'])
def comment_create(request, posting_id):
    posting = get_object_or_404(Posting, id=posting_id)
    comment = Comment()
    comment.posting = posting
    comment.content = request.POST.get('comment')
    comment.save()
    return redirect('board_ad:posting_detail', posting.id)


@require_http_methods(['POST'])
def comment_delete(request, posting_id, comment_id):
    posting = get_object_or_404(Posting, id=posting_id)
    comment = get_object_or_404(Comment, id=comment_id)
    comment.delete()
    return redirect('board_ad:posting_detail', posting.id)
