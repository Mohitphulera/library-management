from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Book, LibraryTransaction
from .forms import BookForm, TransactionForm,UserRegistrationForm
from django.contrib.auth import login, authenticate

@login_required
def issue_book(request):
    if request.method == 'POST':
        form = TransactionForm(request.POST)
        if form.is_valid():
            transaction = form.save(commit=False)
            transaction.transaction_type = 'ISSUE'
            transaction.book.is_available = False
            transaction.book.save()
            transaction.save()
            return redirect('book_list')
    else:
        form = TransactionForm()
    return render(request, 'library/issue_book.html', {'form': form})

@login_required
def return_book(request):
    if request.method == 'POST':
        form = TransactionForm(request.POST)
        if form.is_valid():
            transaction = form.save(commit=False)
            transaction.transaction_type = 'RETURN'
            transaction.book.is_available = True
            transaction.book.save()
            transaction.save()
            return redirect('book_list')
    else:
        form = TransactionForm()
    return render(request, 'library/return_book.html', {'form': form})

@login_required
def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm()
    return render(request, 'library/add_book.html', {'form': form})

@login_required
def remove_book(request, book_id):
    book = Book.objects.get(id=book_id)
    book.delete()
    return redirect('book_list')

@login_required
def book_list(request):
    books = Book.objects.all()
    return render(request, 'library/book_list.html', {'books': books})



def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()  # Load the profile instance created by the signal
            user.email = form.cleaned_data.get('email')
            user.contact_number = form.cleaned_data.get('contact_number')
            user.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)
            return redirect('book_list')
    else:
        form = UserRegistrationForm()
    return render(request, 'library/register.html', {'form': form})
