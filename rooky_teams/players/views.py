from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _
from django.views.generic import (
    ListView, CreateView, UpdateView, DeleteView, DetailView
)
from .models import Player
from rooky_teams.mixins import SuccessMessageMixin
from .forms import PlayerForm


SUCCESS_URL = reverse_lazy('players_index')


class PlayersIndexView(ListView):
    template_name = 'players/index.html'
    model = Player


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
