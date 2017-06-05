from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponse
from django.template import loader
from .models import Author


def index(request):
    template = loader.get_template('index.html')
    context = {}
    return HttpResponse(template.render(context, request))


def authors(request):
    template = loader.get_template('author/index.html')
    context = {
        'entries': Author.objects.all(),
    }
    return HttpResponse(template.render(context, request))
