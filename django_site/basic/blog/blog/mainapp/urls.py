from django.urls import path
from .views import MainListView, ArticleDetailView

urlpatterns = [
    path('', MainListView.as_view(), name='main'),
    path('article/<int:pk>', ArticleDetailView.as_view(), name='article_detail')
]
