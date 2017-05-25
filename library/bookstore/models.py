from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=255)
    born_date = models.DateField()
    death_date = models.DateField()
    description = models.TextField()
