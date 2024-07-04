from django.contrib import admin
from .models import User, AdminUser, Book, LibraryTransaction

admin.site.register(User)
admin.site.register(AdminUser)
admin.site.register(Book)
admin.site.register(LibraryTransaction)
