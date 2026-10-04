from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100 , unique=True)
    explanation = models.TextField()
    next_steps = models.TextField()

    class Meta:
        verbose_name_plural = "categories"
        
    def __str__(self):
        return self.name 