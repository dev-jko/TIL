from django.shortcuts import render, redirect, get_object_or_404, HttpResponseRedirect
from django.views.decorators.http import require_http_methods
from django.contrib.auth.decorators import login_required
from .models import Post, Image, Comment
from .forms import PostModelForm, ImageModelForm, CommentModelForm


@require_http_methods(['GET'])
def post_list(request):
    posts = Post.objects.all()
    comment_form = CommentModelForm()
    return render(request, 'posts/list.html', {
        'posts': posts,
        'comment_form': comment_form,
    })


@login_required
@require_http_methods(['GET', 'POST'])
def create_post(request):
    if request.method == 'POST':
        post_form = PostModelForm(request.POST)
        image_form = ImageModelForm(request.FILES)
        if post_form.is_valid():
            post = post_form.save(commit=False)
            post.user = request.user
            post.save()
            for image in request.FILES.getlist('file'):
                request.FILES['file'] = image
                image_form = ImageModelForm(files=request.FILES)
                if image_form.is_valid():
                    image = image_form.save(commit=False)
                    image.post = post
                    image.save()
            return redirect('posts:post_list')
    else:
        post_form = PostModelForm()
        image_form = ImageModelForm()
    return render(request, 'posts/form.html', {
        'post_form': post_form,
        'image_form': image_form,
    })


@login_required
@require_http_methods(['GET', 'POST'])
def update_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.user != post.user:
        return redirect('posts:post_list')  # forbidden 금지됨
    if request.method == 'POST':
        post_form = PostModelForm(request.POST, instance=post)
        if post_form.is_valid():
            post_form.save()
            return redirect('posts:post_list')
    else:
        post_form = PostModelForm(instance=post)
    return render(request, 'posts/form.html', {
        'post_form': post_form,
    })


@login_required
@require_http_methods(['GET', 'POST'])
def create_comment(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.method == 'POST':
        comment_form = CommentModelForm(data=request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.user = request.user
            comment.save()
            # return redirect('posts:post_list')
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'), '/insta/')
    # else:
    #     comment_form = CommentModelForm()
    # return render()


@login_required
@require_http_methods(['POST'])
def toggle_like(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    user = request.user
    if user in post.like_users.all():
        post.like_users.remove(user)
    else:
        post.like_users.add(user)
    return redirect('posts:post_list')
