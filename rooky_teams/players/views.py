from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _
from django.views.generic import (
    CreateView, UpdateView, DeleteView, DetailView
)
from django_filters.views import FilterView
from .models import Player
from .forms import PlayerForm
from .filters import PlayerFilterSet
from rooky_teams.mixins import SuccessMessageMixin


SUCCESS_URL = reverse_lazy('players_index')


class PlayersIndexView(FilterView):
    template_name = 'players/index.html'
    model = Player
    filterset_class = PlayerFilterSet


class PlayerDetailView(DetailView):
    template_name = 'players/details.html'
    model = Player


class PlayerCreateView(SuccessMessageMixin, CreateView):
    template_name = 'players/create.html'
    model = Player
    form_class = PlayerForm
    success_url = SUCCESS_URL
    success_message = _('Player successfully added!')


class PlayerUpdateView(SuccessMessageMixin, UpdateView):
    template_name = 'players/update.html'
    model = Player
    form_class = PlayerForm
    success_url = SUCCESS_URL
    success_message = _('Player successfully updated!')


class PlayerDeleteView(SuccessMessageMixin, DeleteView):
    template_name = 'players/delete.html'
    model = Player
    success_url = SUCCESS_URL
    success_message = _('Player successfully deleted!')
