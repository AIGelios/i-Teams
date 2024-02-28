from django.utils.translation import gettext_lazy as _
from django.urls import reverse_lazy
from django.views.generic import (
    ListView, DeleteView, TemplateView,
)
from ..mixins import SuccessMessageMixin
from .models import PlayerInRoster
from django.views.decorators.http import require_http_methods
from django.shortcuts import redirect


class RosterPlayersView(ListView):
    template_name = 'players/roster.html'
    model = PlayerInRoster


class RosterPlayerDeleteView(SuccessMessageMixin, DeleteView):
    template_name = 'players/delfromroster.html'
    model = PlayerInRoster
    success_message = _('Player successfully deleted from roster!')
    success_url = reverse_lazy('roster')


class RosterClearView(SuccessMessageMixin, DeleteView):
    pass