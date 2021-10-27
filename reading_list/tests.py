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

	def test_post_content(self):
		self.assertEqual(f'{self.book.title}', 'A good title')
		self.assertEqual(f'{self.book.author}', 'Author of da book')

	def test_post_list_view(self):
		response = self.client.get(reverse('home'))
		self.assertEqual(response.status_code, 200)
		self.assertContains(response, 'Author of da book')
		self.assertTemplateUsed(response, 'home.html')

	def test_post_detail_view(self):
		response = self.client.get('/single_book/1/')
		no_response = self.client.get('/single_book/100000/')
		self.assertEqual(response.status_code, 200)
		self.assertEqual(no_response.status_code, 404)
		self.assertContains(response, 'A good title')
		self.assertTemplateUsed(response, 'single_book.html')