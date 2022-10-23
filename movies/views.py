
from django.shortcuts import render
from .models import Movie, Comment
from django.shortcuts import redirect, get_object_or_404
from django.views.generic import UpdateView



# Create your views here.
def movie(request):
    movies = Movie.objects.all()
    return render(request, 'movies/movie.html',{'movies': movies})

def upload_movie(request):
    if request.method =="POST":
        titles = request.POST['title']
        users = request.user
        images = request.FILES['image']
        videos = request.FILES['video']
        descriptions = request.POST['content']
        movies = Movie.objects.create(title = titles, user = users, image = images, video = videos, description = descriptions)
        movies.save()
        return redirect('movie')
    return render(request, 'movies/upload_movie.html')

def detail_movie(request, movie_id):
    movies = get_object_or_404(Movie,id = movie_id)
    list_comment = Comment.objects.filter(movie = movie_id)
    if request.method =="POST":
        contents = request.POST['comment']
        movies = Movie.objects.get(id = movie_id)
        comments = Comment.objects.create(user = request.user, movie = movies, content = contents)
        comments.save()

    return render(request, 'movies/detail_movie.html',{'movies': movies, 'comments': list_comment})

def find_movie(request):
    find = request.GET.get('find')
    if find:
        movies = Movie.objects.filter(title__icontains = find)
    else:
        movies = Movie.objects.all()
    return render(request, 'movies/movie.html', {'movies': movies})


def delete_movie(request, movie_id):
    movies = get_object_or_404(Movie, pk = movie_id, user = request.user)
    movies.delete()
    return redirect('movie')

