from django.db import models

# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length=200)
    desc = models.TextField(blank=True)
    status = models.BooleanField(default=False)
    task_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title