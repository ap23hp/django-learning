from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    explanation = models.TextField()
    next_steps = models.TextField()

    class Meta:
        verbose_name_plural = "categories"

    def __str__(self):
        return self.name


class Keyword(models.Model):
    word = models.CharField(max_length=100)
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name="keywords",
    )

    def __str__(self):
        return self.word