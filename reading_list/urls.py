from django.urls import path
from .views import (
	ReadingListView, 
	SingleBookView, 
	BookEnterView,
	BookUpdateView,
	BookDeleteView,
)

urlpatterns = [
	path('book/<int:pk>/delete/',
		BookDeleteView.as_view(), name='book_delete'),
	path('book/<int:pk>/edit',
		BookUpdateView.as_view(), name='book_edit'),
	path('book/new/', BookEnterView.as_view(), name='book_new'),
	path('book/<int:pk>/', SingleBookView.as_view(),name='book'),
	path('', ReadingListView.as_view(), name='home'),
]