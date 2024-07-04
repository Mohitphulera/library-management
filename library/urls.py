from django.urls import path
from . import views

urlpatterns = [
    path('add_book/', views.add_book, name='add_book'),
    path('issue_book/', views.issue_book, name='issue_book'),
    path('return_book/', views.return_book, name='return_book'),
    path('', views.book_list, name='book_list'),
    path('remove_book/<int:book_id>/', views.remove_book, name='remove_book'),
    path('register/', views.register, name='register'),
]
