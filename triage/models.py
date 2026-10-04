from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100 , unique=True)
    explanation = models.TextField()
    next_steps = models.TextField()

    def __str__(self):
        return self.name 