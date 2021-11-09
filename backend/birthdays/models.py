from django.db import models
import uuid
from django.conf import settings

# Create your models here.

class Birthday(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    birthday = models.DateField()
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='birthday_registrations'
    )

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-birthday']
