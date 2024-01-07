from django.shortcuts import render
from .models import Movies
# Create your views here.
def index(request):
    movies = Movies.objects.all()
    context = {
        'movies' : movies
    }
    return render(request, 'index.html', context)