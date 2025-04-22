from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _
from django.views.generic import (
    CreateView, UpdateView, DeleteView,
    DetailView, View, ListView, TemplateView,
)
from django_filters.views import FilterView
from .models import Player
from .db_queries import (
    add_to_roster, delete_from_roster, clear_roster,
)
from .forms import PlayerForm
from .filters import PlayerFilterSet
from rooky_teams.mixins import SuccessMessageMixin
from django.shortcuts import redirect
from django.contrib import messages
from django.db import IntegrityError
from .tools import generate_balanced_teams, get_team_ids_json
from ..matches.db_queries import create_match, get_player_matches


PLAYERS_INDEX_URL = reverse_lazy('players_index')


class PlayersIndexView(FilterView):
    template_name = 'players/index.html'
    model = Player
    filterset_class = PlayerFilterSet

    def get_queryset(self):
        return super().get_queryset().order_by('first_name')


class PlayerRosterView(ListView):
    template_name = 'players/roster.html'
    model = Player

    def get_queryset(self):
        return (
            super().get_queryset()
            .filter(is_in_roster=True)
            .order_by('first_name')
        )


class PlayerDetailView(DetailView):
    template_name = 'players/details.html'
    model = Player

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        id = context['player'].id
        context['matches'] = get_player_matches(id)
        return context


class PlayerCreateView(SuccessMessageMixin, CreateView):
    template_name = 'players/create.html'
    model = Player
    form_class = PlayerForm
    success_url = PLAYERS_INDEX_URL
    success_message = _('Player successfully added!')


class PlayerUpdateView(SuccessMessageMixin, UpdateView):
    template_name = 'players/update.html'
    model = Player
    form_class = PlayerForm
    success_url = PLAYERS_INDEX_URL
    success_message = _('Player successfully updated!')


class PlayerDeleteView(SuccessMessageMixin, DeleteView):
    template_name = 'players/delete.html'
    model = Player
    success_url = PLAYERS_INDEX_URL
    success_message = _('Player successfully deleted from database')


class AddToRosrerView(View):
    def post(self, request, *args, **kwargs):
        success_message = _('Player successfully added to the next match')
        error_message = _('Error. Cannot add player to roster!')
        try:
            player_id = kwargs.get('pk')
            add_to_roster(player_id)
            messages.success(self.request, success_message)
        except IntegrityError:
            messages.error(self.request, error_message)
        return redirect(PLAYERS_INDEX_URL)


class DeleteFromRosterView(View):
    def post(self, request, *args, **kwargs):
        success_message = _('Player successfully removed from roster')
        error_message = _('Error. Cannot remove player from roster!')
        try:
            player_id = kwargs.get('pk')
            delete_from_roster(player_id)
            messages.success(self.request, success_message)
        except IntegrityError:
            messages.error(self.request, error_message)
        return redirect(reverse_lazy('roster'))


class RosterClearView(TemplateView):
    template_name = 'players/clear_roster.html'

    def post(self, request, *args, **kwargs):
        success_message = _('Roster successfully cleared')
        error_message = _('Error. Cannot clear roster!')
        try:
            clear_roster()
            messages.success(self.request, success_message)
        except IntegrityError:
            messages.error(self.request, error_message)
        return redirect(reverse_lazy('players_index'))


class GenerateLineupsView(TemplateView):
    template_name = 'players/lineups.html'
    teams = dict(team_1=[], team_2=[])
    
    def get(self, request, *args, **kwargs):
        success_message = _('Lineups generated successfully.')
        too_few_players_message = _(
            'Unable to create teams. Add more players to the roster!')
        self.__class__.teams.update(generate_balanced_teams())
        context = self.__class__.teams
        if not context['team_1'] or not context['team_2']:
            messages.error(self.request, too_few_players_message)
            return redirect(PLAYERS_INDEX_URL)
        messages.success(self.request, success_message)
        return super().get(self, request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        success_message = _('Match successfully created.')+
        context = self.__class__.teams
        match = create_match(
            get_team_ids_json(context['team_1']),
            get_team_ids_json(context['team_2']),
        )
        messages.success(self.request, success_message)
        return redirect(reverse_lazy(
            'match_details', kwargs=dict(pk=match.id)))
