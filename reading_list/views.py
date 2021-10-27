from django.views.generic import ListView, DetailView
from django.views.generic.edit import (
	CreateView, 
	UpdateView,
	DeleteView,
)
from django.urls import reverse_lazy

from .models import Book

class ReadingListView(ListView):
	model = Book
	template_name = 'home.html'
	context_object_name = 'all_books_list'

class SingleBookView(DetailView):
	model = Book
	template_name = 'book.html'
	context_object_name = 'book'

class BookEnterView(CreateView):
	model = Book
	template_name = 'book_entry.html'
	fields = ['title', 'author']

class BookUpdateView(UpdateView):
	model = Book
	template_name = 'book_edit.html'
	fields = ['title', 'author']

class BookDeleteView(DeleteView):
	model = Book
	template_name = 'book_delete.html'
	success_url = reverse_lazy('home')