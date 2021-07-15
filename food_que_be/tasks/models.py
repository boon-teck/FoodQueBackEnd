from django.db import models
from django.db.models.fields import DateTimeField
import uuid
from accounts.models import User

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
    buy_from = models.CharField(max_length=100, blank = True)
    deliver_to = models.CharField(max_length=100, blank = True)
    
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="tasks", blank=True)



    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)