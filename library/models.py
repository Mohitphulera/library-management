from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    contact_number = models.CharField(max_length=15)

class AdminUser(User):
    class Meta:
        proxy = True

class Book(models.Model):
    name = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return self.name

class LibraryTransaction(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    due_date = models.DateField()
    TRANSACTION_TYPE = [
        ('ISSUE', 'Issue'),
        ('RETURN', 'Return'),
    ]
    transaction_type = models.CharField(max_length=6, choices=TRANSACTION_TYPE)
    transaction_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.book.name} - {self.transaction_type}"
