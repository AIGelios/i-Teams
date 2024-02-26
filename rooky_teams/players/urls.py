from .views import (
    PlayersIndexView,
    PlayerDetailView,
    PlayerCreateView,
    PlayerUpdateView,
    PlayerDeleteView,
)
from django.urls import path


urlpatterns = [
    path('', PlayersIndexView.as_view(), name='players_index'),
    path('<int:pk>/', PlayerDetailView.as_view(), name='player_details'),
    path('create/', PlayerCreateView.as_view(), name='player_create'),
    path('<int:pk>/update/', PlayerUpdateView.as_view(), name='player_update'),
    path('<int:pk>/delete/', PlayerDeleteView.as_view(), name='player_delete'),
]
