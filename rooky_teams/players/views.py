from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _
from django.views.generic import (
    CreateView, UpdateView, DeleteView, DetailView, View
)
from django_filters.views import FilterView
from .models import Player
from ..roster.models import PlayerInRoster
from .forms import PlayerForm
from .filters import PlayerFilterSet
from rooky_teams.mixins import SuccessMessageMixin
from django.shortcuts import redirect
from django.contrib import messages
from django.db import IntegrityError


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
    success_message = _('Player successfully deleted from database!')


class AddToRosrerView(View):
    def post(self, request, *args, **kwargs):
        success_message = _('Player successfully added to the next match!')
        error_message = _('Error. Cannot add player to roster!')
        id = kwargs.get('pk')
        try:
            PlayerInRoster.objects.create(player_id=id)
            messages.success(self.request, success_message)
        except IntegrityError:
            messages.error(self.request, error_message)
        return redirect(SUCCESS_URL)
