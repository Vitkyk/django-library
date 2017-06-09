from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.template import loader
from .models import Author, Book
from .forms import BookForm


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


def books(request):
    return render(
        request,
        'book/index.html',
        {'entries': Book.objects.all()}
    )


def book_detail(request, id=1):
    return render(
        request,
        'book/detail.html',
        {'item': Book.objects.get(pk=id)}
    )


def book_new(request):
    if request.method == 'POST':
        book = Book()
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = BookForm()
    return render(
        request,
        'book/form.html',
        {'form': form}
    )
