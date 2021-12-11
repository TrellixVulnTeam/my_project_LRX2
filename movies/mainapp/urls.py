from django.contrib import admin
from django.urls import path
from .views import MoviesListView, MovieDetailView, AddReview, ActorDetailView, FilterMovieView

urlpatterns = [
    path('', MoviesListView.as_view(), name='index'),
    path('filter/', FilterMovieView.as_view(), name='filter'),
    path('<slug:slug>/', MovieDetailView.as_view(), name='movie_detail'),
    path('review/<int:pk>/', AddReview.as_view(), name='add_review'),
    path('actor/<str:slug>/', ActorDetailView.as_view(), name='actor_detail')

]
