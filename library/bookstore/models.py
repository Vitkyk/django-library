from django.contrib.auth.models import User
from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from behaviors.behaviors import Authored, Timestamped, Published


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    description = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)


class Author(models.Model):
    name = models.CharField(max_length=255)
    born_date = models.DateField()
    death_date = models.DateField()
    description = models.TextField()


class Book(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)


class BookOnHands(models.Model):
    user = models.OneToOneField(User)
    book = models.OneToOneField(Book)
    issue_date = models.DateField()
    return_date = models.DateField()


class History(models.Model):
    user = models.OneToOneField(User)
    book = models.OneToOneField(Book)
    start_date = models.DateField()
    end_date = models.DateField()


class Comment(Authored, Timestamped, models.Model):
    book = models.OneToOneField(Book)
    text = models.CharField(max_length=200)


class Like(Authored, Timestamped, models.Model):
    book = models.OneToOneField(Book)


class Dislike(Authored, Timestamped, models.Model):
    book = models.OneToOneField(Book)
