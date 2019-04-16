from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_http_methods
from .models import Writer, Book, Chapter
from .forms import *


@require_http_methods(['GET', 'POST'])
def create(request):
    if request.method == 'POST':
        form = WriterModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect()
    else:
        form = WriterModelForm()
    return render(request, 'onetomany/form.html', {
        'form': form,
    })


@require_http_methods(['GET', 'POST'])
def update(request, id):
    writer = get_object_or_404(Writer, id=id)
    if request.method == 'POST':
        form = WriterModelForm(request.POST, instance=writer)
        if form.is_valid():
            form.save()
            return redirect()
    else:
        form = WriterModelForm(instance=writer)
    return render(request, 'onetomany/form.html', {
        'form': form,
    })


def list(request):
    writers = Writer.objects.all()
    return render(request, 'onetomany/list.html', {
        'writers': writers,
    })
