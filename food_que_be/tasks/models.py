from django.db import models
from django.db.models.fields import DateTimeField
import uuid

# Create your models here.
class Task(models.Model):
    id = models.UUIDField(
        primary_key=True,
        editable=False,
        default=uuid.uuid4
    )
    name_of_task = models.CharField(max_length=50)
    description_to_buy = models.TextField(max_length=5000)
    cost_of_food = models.IntegerField()
    budget = models.IntegerField()
    is_completed = models.BooleanField(default=False)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)