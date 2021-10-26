from django.test import TestCase
from .models import Book

class BookModelTest(TestCase):
	def setUp(self):
		Book.objects.create(title='just a test')
		Book.objects.create(author='yet another test')

	def test_title_content(self):
		book=Book.objects.get(id=1)
		expected_object_name = f'{book.title}'
		self.assertEqual(expected_object_name, 'just a test')
