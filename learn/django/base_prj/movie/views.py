from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Movie
from .forms import MovieModelForm


# Create your views here.

def index(request):
    movies = Movie.objects.all()
    return render(request, 'movie/list.html', {'movies': movies})


@login_required(login_url='accounts:signin')
def create(request):
    if request.method == 'POST':
        form = MovieModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('movie:list')
    else:
        form = MovieModelForm()
    return render(request, 'movie/create.html', {'form': form})


def update(request, id):
    movie = get_object_or_404(Movie, id=id)
    if request.method == 'POST':
        form = MovieModelForm(request.POST, instance=movie)
        if form.is_valid():
            form.save()
            return redirect('movie:detail', id)
    else:
        form = MovieModelForm(instance=movie)
    return render(request, 'movie/update.html', {'form': form})
