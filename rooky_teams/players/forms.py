from django.forms import ModelForm
from .models import Player
from django.utils.translation import gettext_lazy as _


class PlayerForm(ModelForm):
    class Meta:
        model = Player
        fields = (
            'first_name',
            'last_name',
            'role',
            'gk_skill',
            'def_skill',
            'frw_skill',
        )
        labels = dict(
            first_name=_('First name'),
            last_name=_('Last name'),
            role=_('Role on the field'),
            gk_skill=_('Goalkeeper skill'),
            def_skill=_('Defender skill'),
            frw_skill=_('Forward skill'),
        )
