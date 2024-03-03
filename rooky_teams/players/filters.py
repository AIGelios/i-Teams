import django_filters
from .models import Player, Roles
from django.utils.translation import gettext_lazy as _


class PlayerFilterSet(django_filters.FilterSet):
    role = django_filters.ChoiceFilter(
        choices=Roles.choices,
        label=_('Filter by role on the field'),
    )

    class Meta:
        model = Player
        fields = ['role']
