from django.urls import path
from .views import ReadingListView, SingleBookView

urlpatterns = [
	path('single_book/<int:pk>/', SingleBookView.as_view(),name='single_book'),
	path('', ReadingListView.as_view(), name='home'),
]