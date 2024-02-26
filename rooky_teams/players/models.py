from django.db import models
from rooky_teams.roles.models import Role
from rooky_teams.skills.models import SkillLevel


class Player(models.Model):
    first_name = models.CharField(
        max_length=64,
    )
    last_name = models.CharField(
        max_length=64,
    )
    role = models.ForeignKey(
        to=Role,
        on_delete=models.PROTECT,
        blank=False,
        null=False,
        related_name='role'
    )
    gk_skill = models.ForeignKey(
        to=SkillLevel,
        on_delete=models.PROTECT,
        blank=False,
        null=False,
        related_name='gk_skill'
    )
    def_skill = models.ForeignKey(
        to=SkillLevel,
        on_delete=models.PROTECT,
        blank=False,
        null=False,
        related_name='def_skill'
    )
    off_skill = models.ForeignKey(
        to=SkillLevel,
        on_delete=models.PROTECT,
        blank=False,
        null=False,
        related_name='off_skill'
    )

    @property
    def avg_skill(self):
        return round(sum((
            self.gk_skill.value,
            self.def_skill.value,
            self.off_skill.value,
        )) / 3, 2)

    def __str__(self):
        return f'{self.first_name} {self.last_name} ({self.avg_skill})'
