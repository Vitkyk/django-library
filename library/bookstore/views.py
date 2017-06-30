from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.template import loader
from .models import Author, Book, Comment
from .forms import BookForm, CommentForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

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
    book_list = Book.objects.all()
    paginator = Paginator(book_list, 1) # Show 25 contacts per page

    page = request.GET.get('page')
    try:
        paginated_book_list = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        paginated_book_list = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        paginated_book_list = paginator.page(paginator.num_pages)

    return render(
        request,
        'book/index.html',
        {'entries': paginated_book_list, 'range': range(1, 3)}
    )


def book_detail(request, book_id=1):
    return render(
        request,
        'book/detail.html',
        {
            'book': Book.objects.get(pk=book_id),
            'comments': Comment.objects.filter(book=book_id),
            #'comments': Comment.objects.all(),
            'form': CommentForm(),
        }
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


def comment_new(request, book_id=1):
    if request.method == 'POST':
        comment = Comment()
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.book = Book(id=book_id)
            obj.author = request.user
            obj.save()
            return redirect('book_detail', book_id=book_id)
    else:
        form = CommentForm()
    return render(
        request,
        'book/detail.html',
        {
            'book': Book.objects.get(pk=book_id),
            'comments': Comment.objects.all(),
            'form': form,
        }
    )
