from django.db import models

class Repository(models.Model):
    name = models.CharField(max_length=100)
    stars = models.PositiveIntegerField()