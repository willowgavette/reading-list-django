from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from .models import Book

class BlogTests(TestCase):
	def setUp(self):
		self.user = get_user_model().objects.create_user(
			username='testuser',
			email='test@email.com',
			password='secret'
			)
		self.book = Book.objects.create(
			title='A good title',
			author="Author of da book"			
			)

	def test_string_representation(self):
		book = Book(title='A sample title')
		self.assertEqual(str(book), book.title)

	def test_book_content(self):
		self.assertEqual(f'{self.book.title}', 'A good title')
		self.assertEqual(f'{self.book.author}', 'Author of da book')

	def test_book_list_view(self):
		response = self.client.get(reverse('home'))
		self.assertEqual(response.status_code, 200)
		self.assertContains(response, 'Author of da book')
		self.assertTemplateUsed(response, 'home.html')

	def test_book_detail_view(self):
		response = self.client.get('/book/1/')
		no_response = self.client.get('/book/100000/')
		self.assertEqual(response.status_code, 200)
		self.assertEqual(no_response.status_code, 404)
		self.assertContains(response, 'A good title')
		self.assertTemplateUsed(response, 'book.html')

	def test_book_create_view(self):
		response = self.client.post(reverse('book_new'), {
			'title': 'New title',
			'author': 'New author',
			})
		self.assertEqual(response.status_code, 302)
		self.assertEqual(Book.objects.last().title, 'New title')
		self.assertEqual(Book.objects.last().author, 'New author')

	def test_book_update_view(self):
		response = self.client.post(reverse('book_edit', args='1'), {
			'title': 'Updated title',
			'author': 'Updated author',
			})
		self.assertEqual(response.status_code, 302)

	def test_book_delete_view(self):
		response = self.client.post(reverse('book_delete', args='1'))
		self.assertEqual(response.status_code, 302)