from django.shortcuts import render
from projectapp.models import Book
# Create your views here.
def book_save(request):
    book = Book.objects.create(
        name = 'mehrobdan chayoy'
    )
