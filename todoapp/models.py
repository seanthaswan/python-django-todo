from django.db import models
from django.contrib.auth.models import User

class Todo(models.Model):
  text = models.CharField(max_length=250)
  is_complete = models.BooleanField(default=False)
  user = models.ForeignKey(User, on_delete=models.CASCADE, blank=False, null=False)

  def __str__(self):
    return self.text