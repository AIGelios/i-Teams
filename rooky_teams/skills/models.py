from django.db import models
from django.utils.translation import gettext as _


TRANSLATED_NAMES = {
    1: _('very bad'),
    2: _('bad'),
    3: _('medium'),
    4: _('good'),
    5: _('excellent')
}


class SkillLevel(models.Model):
    value = models.IntegerField()
    
    def __str__(self):
        return f'{TRANSLATED_NAMES.get(self.value)} ({self.value})'
