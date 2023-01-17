from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    price = models.PositiveIntegerField(default=0)
    read = models.BooleanField(default=False)

    def __str__(self):
        return self.title
