from django.urls import path
from .views import movie, upload_movie, detail_movie, find_movie, delete_movie
urlpatterns = [
    path('',movie , name='movie'),
    path('upload', upload_movie, name='upload'),
    path('movie/<int:movie_id>', detail_movie, name='detail_movie'),
     path('movie/<int:movie_id>/delete', delete_movie, name='delete_movie'),
    path('movie/find', find_movie, name='find_movie')
]