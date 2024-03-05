from django.forms import ModelForm, DateInput
from .models import Match
from django.utils.translation import gettext_lazy as _


class MatchForm(ModelForm):
    class Meta:
        model = Match
        fields = (
            'match_date',
            'team_1_goals',
            'team_2_goals',
            'description',
        )
        labels = dict(
            match_date=_('Date of the match'),
            team_1_goals=_('Team 1 goals'),
            team_2_goals=_('Team 2 goals'),
            description=_('Notes about match'),
        )
        widgets = {
            'match_date': DateInput(
                format="%Y-%m-%d",
                attrs={"type": "date"},
            )
        }
