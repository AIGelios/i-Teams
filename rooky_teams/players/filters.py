from django.utils.translation import gettext_lazy as _
import django_filters
from rooky_teams.roles.models import Role
from .models import Player


class PlayerFilterSet(django_filters.FilterSet):
    role = django_filters.ModelChoiceFilter(
        queryset=Role.objects.all(),
        required=False,
        label=_('Filter by role:'),
    )

    class Meta:
        model = Player
        fields = []
