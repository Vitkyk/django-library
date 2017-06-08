from django.contrib import admin
from .models import Profile, Author, Book, BookOnHands, History, Comment, Like, Dislike, BookInstance

admin.site.register(Profile)
admin.site.register(Author)
admin.site.register(Book)
admin.site.register(BookInstance)
admin.site.register(BookOnHands)
admin.site.register(History)
admin.site.register(Comment)
admin.site.register(Like)
admin.site.register(Dislike)
