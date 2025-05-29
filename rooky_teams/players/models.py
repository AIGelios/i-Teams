from django.db import models
from django.utils.translation import gettext_lazy as _


ROLES_CHOICES = (
    (1, _('Goalkeeper')),
    (2, _('Defender')),
    (3, _('Forward')),
)


SKILLS_CHOICES = (
    (1, _('1 - Very bad')),
    (2, _('2 - Bad')),
    (3, _('3 - Medium')),
    (4, _('4 - Good')),
    (5, _('5 - Excellent')),
)

TEAM_CHOICES = (
    (0, _('No team')),
    (1, _('Team 1')),
    (2, _('Team 2')),
)


class Player(models.Model):
    first_name = models.CharField(
        max_length=64,
    )
    last_name = models.CharField(
        max_length=64,
    )
    role = models.SmallIntegerField(
        choices=ROLES_CHOICES,
    )
    gk_skill = models.SmallIntegerField(
        choices=SKILLS_CHOICES,
    )
    def_skill = models.SmallIntegerField(
        choices=SKILLS_CHOICES,
    )
    frw_skill = models.SmallIntegerField(
        choices=SKILLS_CHOICES,
    )
    is_in_roster = models.BooleanField(
        default=False,
        null=False,
    )
    team = models.SmallIntegerField(
        choices=TEAM_CHOICES,
        default=0,
        null=0,
    )

    @property
    def role_name(self):
        return dict(ROLES_CHOICES)[self.role]

    @property
    def avg_skill(self):
        return round(sum([
            self.gk_skill,
            self.def_skill,
            self.frw_skill,
        ]) / 3, 1)

    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'

    def __str__(self):
        return f'{self.full_name} ({self.avg_skill})'
