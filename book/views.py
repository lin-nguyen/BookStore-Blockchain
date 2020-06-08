from django.views.generic import ListView, DetailView
from thuvienbk.models import Book, BookAuthor
from django.shortcuts import get_object_or_404

class BookListView(ListView):
    model = Book
    template_name = 'book/book_list.html'
    context_object_name = 'books'
    ordering = ['-sales_volume']
    paginate_by = 1


class SearchedBookListView(ListView):
    model = Book
    template_name = 'book/searched_book.html'
    context_object_name = 'books'

    def get_queryset(self):
        title = self.request.GET['title']
        return Book.objects.filter(title__icontains=title).order_by('-sales_volume')


# class AuthorBooksListView(ListView):
#     model = Book
#     template_name = 'book/author_books.html'
#     context_object_name = 'books'
#     paginate_by = 2
#
#     def get_queryset(self):
#         authors = get_object_or_404(BookAuthor)
#         author = get_object_or_404(BookAuthor, author_name=self.kwargs.get('author_name'))
#         return Book.objects.filter(author=author).order_by('-sales_volume')
#
#
# class BookDetailView(DetailView):
#     model = Book
#     template_name = 'book/book_detail.html'
#     context_object_name = 'book'
