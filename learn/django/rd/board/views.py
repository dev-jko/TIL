from django.shortcuts import render, redirect
from .models import Movie
# Create your views here.


def board_list(request):
    movies = Movie.objects.all()
    return render(request, 'board_ad/list.html', {'movies': movies})


def board_detail(request, id):
    movie = Movie.objects.get(id=id)
    return render(request, 'board_ad/detail.html', {'movie': movie})


def board_delete(request, id):
    movie = Movie.objects.get(id=id)
    movie.delete()
    return redirect('board_ad:board_list')
