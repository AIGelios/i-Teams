from django.views.generic import (
    ListView, UpdateView, DeleteView,
    DetailView, View,
)
from .models import Match
from .db_queries import create_match_manually
from ..mixins import SuccessMessageMixin
from .forms import MatchForm
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _


MATCHES_INDEX_URL = reverse_lazy('matches_index')


class MatchesIndexView(ListView):
    template_name = 'matches/index.html'
    model = Match

    def get_queryset(self):
        return super().get_queryset().order_by('-match_date')


class MatchDetailsView(DetailView):
    template_name = 'matches/details.html'
    model = Match


class MatchUpdateView(SuccessMessageMixin, UpdateView):
    template_name = 'matches/update.html'
    model = Match
    form_class = MatchForm
    success_message = _('Match information updated sucessfully.')

    @property
    def success_url(self):
        match_id = self.get_context_data()['match'].id
        return reverse_lazy('match_details', kwargs=dict(pk=match_id))


class MatchDeleteView(SuccessMessageMixin, DeleteView):
    template_name = 'matches/delete.html'
    model = Match
    success_url = MATCHES_INDEX_URL
    success_message = _('Match deleted sucessfully.')
