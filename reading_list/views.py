from django.views.generic import ListView
from .models import Book

class HomePageView(ListView):
	model = Book
	template_name = 'home.html'
	context_object_name = 'all_books_list'