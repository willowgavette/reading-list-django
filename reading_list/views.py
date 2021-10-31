from django.contrib.auth.mixins import (
	LoginRequiredMixin,
	UserPassesTestMixin
)
from django.views.generic import ListView, DetailView
from django.views.generic.edit import (
	CreateView, 
	UpdateView,
	DeleteView,
)
from django.urls import reverse_lazy

from .models import Book

class ReadingListView(LoginRequiredMixin, ListView):
	model = Book
	template_name = 'home.html'
	context_object_name = 'all_books_list'

class SingleBookView(LoginRequiredMixin, DetailView):
	model = Book
	template_name = 'book.html'
	context_object_name = 'book'

class BookEnterView(LoginRequiredMixin, CreateView):
	model = Book
	template_name = 'book_entry.html'
	fields = ['title', 'book_author', 'year', 'isbn', 'completed']

	def form_valid(self, form):
		form.instance.author = self.request.user
		return super().form_valid(form)

class BookUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
	model = Book
	template_name = 'book_edit.html'
	fields = ['title', 'book_author', 'year', 'isbn', 'completed']

	def test_func(self):
		obj = self.get_object()
		return obj.author == self.request.user

class BookDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
	model = Book
	template_name = 'book_delete.html'
	success_url = reverse_lazy('home')

	def test_func(self):
		obj = self.get_object()
		return obj.author == self.request.user