from django.conf import settings
from django.db import models
from django_extensions.db.models import TimeStampedModel
import uuid

from apps.users.models.profile import Profile


class Coach(TimeStampedModel):
    """
    A person who offers direction, instruction and training to a sports team or of individual sports people
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.OneToOneField(
        Profile,
        on_delete=models.CASCADE
    )

    class Meta:
        verbose_name = "Coach"
        verbose_name_plural = "Coaches"
        db_table = 'coach'

    def __str__(self):
        return self.name
