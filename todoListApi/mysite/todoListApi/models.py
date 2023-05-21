from django.db import models


# Create your models here.
class TodoList(models.Model):
    title = models.CharField(max_length=50, null=False)
    content = models.TextField(null=False)
    detail = models.TextField(null=False)
    is_completed = models.BooleanField(default=False)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
