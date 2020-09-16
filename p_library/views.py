from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.views.generic import ListView

from p_library.models import Book


class BookTablePage(ListView):
    model = Book


def book_increment(request):
    if request.method == 'POST':
        book_id = request.POST['id']
        if not book_id:
            return redirect('/')
        else:
            book = Book.objects.filter(id=book_id).first()
            if not book:
                return redirect('/')
            book.copy_count += 1
            book.save()
        return redirect('/')
    else:
        return redirect('/')


def book_decrement(request):
    if request.method == 'POST':
        book_id = request.POST['id']
        if not book_id:
            return redirect('/')
        else:
            book = Book.objects.filter(id=book_id).first()
            if not book:
                return redirect('//')
            if book.copy_count < 1:
                book.copy_count = 0
            else:
                book.copy_count -= 1
            book.save()
        return redirect('/')
    else:
        return redirect('/')