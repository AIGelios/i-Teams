from .views import (
    MatchesIndexView,
    MatchDetailsView,
    MatchDeleteView,
    MatchUpdateView,
)
from django.urls import path


urlpatterns = [
    path('', MatchesIndexView.as_view(), name='matches_index'),
    path('<int:pk>/details', MatchDetailsView.as_view(), name='match_details'),
    path('<int:pk>/delete', MatchDeleteView.as_view(), name='match_delete'),
    path('<int:pk>/update', MatchUpdateView.as_view(), name='match_update'),
]
