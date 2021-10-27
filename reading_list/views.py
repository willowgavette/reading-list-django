from django.views.generic import ListView, DetailView
from .models import Book

class ReadingListView(ListView):
	model = Book
	template_name = 'home.html'
	context_object_name = 'all_books_list'

class SingleBookView(DetailView):
	model = Book
	template_name = 'single_book.html'
	context_object_name = 'book'