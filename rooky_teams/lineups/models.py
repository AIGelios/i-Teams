from django.db import models


class LineUp(models.Model):
    blue_team = models.CharField(
        max_length=255
    )
    blue_team = models.CharField(
        max_length=255
    )
    created_at = models.DateTimeField(
        auto_now_add=True
    )
