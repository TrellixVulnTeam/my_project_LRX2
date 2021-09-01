from django.urls import path
from .views import index, PlayerCreateView, PlayerUpdateView

urlpatterns = [
    path('add', PlayerCreateView.as_view(), name='add'),
    path('<int:pk>/', PlayerUpdateView.as_view(), name='update'),
    path('', index, name='index'),
]
