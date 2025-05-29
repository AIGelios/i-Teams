from .views import (
    PlayersIndexView,
    PlayerRosterView,
    PlayerDetailView,
    PlayerCreateView,
    PlayerUpdateView,
    PlayerDeleteView,
    AddToRosrerView,
    DeleteFromRosterView,
    RosterClearView,
    GenerateLineupsView,
    ManualTeamsView,
)
from django.urls import path


urlpatterns = [
    path('', PlayersIndexView.as_view(), name='players_index'),
    path('roster/', PlayerRosterView.as_view(), name='roster'),
    path('<int:pk>/', PlayerDetailView.as_view(), name='player_details'),
    path('create/', PlayerCreateView.as_view(), name='player_create'),
    path(
        '<int:pk>/update/',
        PlayerUpdateView.as_view(),
        name='player_update'),
    path(
        '<int:pk>/delete/',
        PlayerDeleteView.as_view(),
        name='player_delete'),
    path(
        '<int:pk>/add_to_roster/',
        AddToRosrerView.as_view(),
        name='add_to_roster'),
    path(
        '<int:pk>/delete_from_roster/',
        DeleteFromRosterView.as_view(),
        name='delete_from_roster'),
    path(
        'roster/clear/',
        RosterClearView.as_view(),
        name='clear_roster'),
    path('lineups/',
         GenerateLineupsView.as_view(),
         name='lineups'),
    path('manual_teams/', ManualTeamsView.as_view(), name='manual_teams'),
]
