from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('search', views.search, name = 'search'),
    path('add_book', views.add_book, name = 'add_book'),
    path('delete/<int:book_id>/', views.delete_book, name='delete_book'),
]