from django.db import models
from django.utils.translation import gettext as _


class Roles(models.IntegerChoices):
    GOALKEEPER = (1, _('Goalkeeper'))
    DEFENDER = (2, _('Defender'))
    FORWARD = (3, _('Forward'))


class Skills(models.IntegerChoices):
    VERY_BAD = (1, _('1 - Very bad'))
    BAD = (2, _('2 - Bad'))
    MEDIUM = (3, _('3 - Medium'))
    GOOD = (4, _('4 - Good'))
    EXCELLENT = (5, _('5 - Excellent'))


class Player(models.Model):
    first_name = models.CharField(
        max_length=64,
    )
    last_name = models.CharField(
        max_length=64,
    )
    role = models.SmallIntegerField(
        choices=Roles.choices,
    )
    gk_skill = models.SmallIntegerField(
        choices=Skills.choices,
    )
    def_skill = models.SmallIntegerField(
        choices=Skills.choices,
    )
    frw_skill = models.SmallIntegerField(
        choices=Skills.choices
    )
    is_in_roster = models.BooleanField(
        default=False,
        null=False
    )

    @property
    def role_name(self):
        return dict(Roles.choices)[self.role]

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
