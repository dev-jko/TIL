from django.shortcuts import render, redirect, get_object_or_404

from .models import Posting, Comment


# Create your views here.


def posting_list(request):
    postings = Posting.objects.all()
    return render(request, 'sns/list.html', {'postings': postings})


def create_posting(request):
    if request.method == 'GET':
        return redirect('sns:posting_list')
    else:
        data = request.POST.get
        posting = Posting()
        posting.content = data('content')
        posting.icon = data('icon')
        posting.image = request.FILES.get('image')
        posting.save()
        return redirect('sns:posting_detail', posting.id)


def posting_detail(request, posting_id):
    posting = get_object_or_404(Posting, id=posting_id)
    comments = posting.comment_set.all()
    return render(request, 'sns/detail.html', {'posting': posting, 'comments': comments})


def edit_posting(request):
    return None


def delete_posting(request):
    return None
