from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=64)
    author = models.CharField(max_length=64)
    pages = models.IntegerField(blank=True, null=True)
    category = models.CharField(default="C001", max_length=4)