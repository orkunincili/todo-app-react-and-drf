from django.db import models

# Create your models here.


class Todo(models.Model):
    """Database model for todos in th system"""
    PRIORITY_CHOICES = (
        ("1", "Low"),
        ("2", "Normal"),
        ("3", "High")
    )
    title = models.CharField(max_length=255)
    priority = models.CharField(max_length=6, choices=PRIORITY_CHOICES, default="1")
    status = models.BooleanField(default=False)
    creation_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):

        return self.title
