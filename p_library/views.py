from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.db.models import Count
from django.urls import reverse_lazy
from django.forms import formset_factory


from p_library.models import Book, Author, Publisher, Friend
from p_library.forms import AuthorForm, BookForm


def index(request):
    message = 'Welcome to my library!'

    return HttpResponse(message)


def books_list(request):
    books = Book.objects.all()

    return HttpResponse(books)


def authors_list(request):
    authors = Author.objects.all()

    return HttpResponse(authors)


def friends_list(request):
    template = loader.get_template('friends.html')
    friends = Friend.objects.all()
    data = {
        'friends': friends,
    }

    return HttpResponse(template.render(data))


def publishers_list(request):
    template = loader.get_template('publishers.html')
    publishers = Publisher.objects.annotate(books_count=Count('book_publisher'))
    data = {
        'publishers': publishers, 
    }

    return HttpResponse(template.render(data))    


def book_increment(request):
    if request.method == 'POST':
        book_id = request.POST['id']
        if not book_id:
            return redirect('/books_table/')
        else:
            book = Book.objects.filter(id=book_id).first()
            if not book:
                return redirect('/books_table/')
            book.copy_count += 1
            book.save()
        return redirect('/books_table/')
    else:
        return redirect('/books_table/')


def book_decrement(request):
    if request.method == 'POST':
        book_id = request.POST['id']
        if not book_id:
            return redirect('/books_table/')
        else:
            book = Book.objects.filter(id=book_id).first()
            if not book:
                return redirect('/books_table/')
            if book.copy_count < 1:
                book.copy_count = 0
            else:
                book.copy_count -= 1
            book.save()
        return redirect('/books_table/')
    else:
        return redirect('/books_table/')


def books_table(request):
    template = loader.get_template("books_table.html")
    books = Book.objects.all()
    biblio_data = {
        "title": "мою библиотеку",
        "books": books,
    }

    return HttpResponse(template.render(biblio_data, request))


def book_create_many(request):
    BookFormSet = formset_factory(BookForm, extra=2)

    if request.method == 'POST':
        book_formset = BookFormSet(request.POST, request.FILES, prefix='books')

        if book_formset.is_valid():
            for book_form in book_formset:
                book_form.save()

            return HttpResponseRedirect(reverse_lazy('author_list'))

    else:
        book_formset = BookFormSet(prefix='books')

    return render(request, 'manage_books.html', {'book_formset': book_formset})


def author_create_many(request):
    AuthorFormSet = formset_factory(AuthorForm, extra=2)

    if request.method == 'POST':
        author_formset = AuthorFormSet(request.POST, request.FILES, prefix='authors')

        if author_formset.is_valid():
            for author_form in author_formset:
                author_form.save()

            return HttpResponseRedirect(reverse_lazy('author_list'))

    else:
        author_formset = AuthorFormSet(prefix='authors')

    return render(request, 'manage_authors.html', {'author_formset': author_formset})