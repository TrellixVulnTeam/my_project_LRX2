from django.contrib import admin
from django.urls import path
from .views import MoviesListView, MovieDetailView, AddReview

urlpatterns = [
    path('', MoviesListView.as_view(), name='index'),
    path('<slug:slug>/', MovieDetailView.as_view(), name='movie_detail'),
    path('review/<int:pk>/', AddReview.as_view(), name='add_review')
]
