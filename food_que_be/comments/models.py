from django.db import models
from django.db.models.fields import DateTimeField
import uuid
from tasks.models import Task

# Create your models here.
class Comment(models.Model):
    id = models.UUIDField(
        primary_key=True,
        editable=False,
        default=uuid.uuid4
    )
    comment_content = models.CharField(max_length=5000)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    task = models.ForeignKey(
        Task,
        on_delete=models.CASCADE,
        related_name="comments")
    