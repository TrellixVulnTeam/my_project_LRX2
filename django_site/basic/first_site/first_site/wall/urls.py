from django.urls import path
from .views import index, by_rubric, WallCreateView

urlpatterns = [
    path('add/', WallCreateView.as_view(), name='add'),
    path('<int:rubric_id>/', by_rubric, name='by_rubric'),
    path('', index, name='index')
]
