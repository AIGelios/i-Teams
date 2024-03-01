import django_filters
from .models import Player


class PlayerFilterSet(django_filters.FilterSet):
    class Meta:
        model = Player
        fields = ['role']
