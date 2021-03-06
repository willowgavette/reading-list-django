from django.db import models
from django.urls import reverse

class Book(models.Model):
	title = models.CharField(max_length=100)
	book_author = models.CharField(max_length=100)
	year = models.IntegerField()
	isbn = models.IntegerField(null=True, blank=True)
	completed = models.BooleanField(default=False)

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse('book', args=[str(self.id)])