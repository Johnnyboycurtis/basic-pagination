from django.db import models
import datetime

class ToDoList(models.Model):
    name = models.CharField(max_length=50, blank=True, choices = [('user1', 'user1'), ('user2', 'user2')])
    text = models.TextField(blank=True, default="something something ...")
    due_date = models.DateField(default = datetime.date.today)

