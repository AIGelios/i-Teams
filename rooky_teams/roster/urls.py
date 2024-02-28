from django.urls import path
from .views import (
    RosterPlayersView, RosterPlayerDeleteView, RosterClearView,
)


urlpatterns = [
    path('', RosterPlayersView.as_view(), name='roster'),
    path(
        '<int:pk>/delete/',
        RosterPlayerDeleteView.as_view(),
        name='delete_from_roster',
    ),
    path('clean/', RosterClearView.as_view(), name='clear_roster')
]
