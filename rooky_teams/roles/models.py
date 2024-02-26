from django.db import models
from django.utils.translation import gettext as _


ROLES = {
    'Goalkeeper': _('Goalkeeper'),
    'Defender': _('Defender'),
    'Forward': _('Forward')
}


class Role(models.Model):
    name = models.CharField(
        max_length=64,
        unique=True,
        blank=False,
    )

    def __str__(self):
        return ROLES.get(self.name)
