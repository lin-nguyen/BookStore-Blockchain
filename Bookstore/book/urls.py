from django.urls import path
from .views import BookListView, SearchedBookListView

urlpatterns = [
    path('', BookListView.as_view(), name='books-list'),
    path('search/search', SearchedBookListView.as_view(), name='searched-book'),
    # path('book/<int:pk>/', BookDetailView.as_view(), name='book-detail'),
]
