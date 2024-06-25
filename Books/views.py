from django.shortcuts import render, redirect, get_object_or_404
from .forms import BookForm
from django.contrib.auth.decorators import login_required, user_passes_test
from django.http import HttpResponseRedirect
from .models import Book
@login_required(login_url='login_user')
def search(request):
    if request.method == "POST":
        searched = request.POST['searched']
        books = Book.objects.filter(title__contains = searched) 
        return render(request, 'search.html', {'searched' :searched, 'books':books})
    else:
        return render(request, 'search.html', {'searched' :searched})

def is_superuser(user):
    return user.is_superuser

@login_required(login_url='login_user')
@user_passes_test(is_superuser)
def delete_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    pdf_path = book.pdf.path
    book.delete()

    import os
    if os.path.exists(pdf_path):
        os.remove(pdf_path)
    return redirect('index')

@login_required(login_url='login_user')
@user_passes_test(is_superuser)
def add_book(request):
    submitted = False

    if request.method == "POST":
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/?submitted=True')
    else:
        form = BookForm()
        if 'submitted' in request.GET:
            submitted = True

    return render(request, 'add_book.html', {'form': form, 'submitted': submitted})

@login_required(login_url='login_user')
def index(request):
    books = Book.objects.all()
    return render(request, 'index.html',{'book_list': books})
    
