from django.db import models
from ..players.models import Player


class PlayerInRoster(models.Model):
    player = models.OneToOneField(
        to=Player,
        on_delete=models.CASCADE,
    )
