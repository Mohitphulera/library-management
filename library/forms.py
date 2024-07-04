from django import forms
from .models import Book, LibraryTransaction,User

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['name', 'author', 'is_available']

class TransactionForm(forms.ModelForm):
    class Meta:
        model = LibraryTransaction
        fields = ['user', 'book', 'due_date', 'transaction_type']


from django.contrib.auth.forms import UserCreationForm

class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    contact_number = forms.CharField(max_length=15)

    class Meta:
        model = User
        fields = ['username', 'email', 'contact_number', 'password1', 'password2']
