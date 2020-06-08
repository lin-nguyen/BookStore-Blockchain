from django.urls import path
from book.api.views import api_detail_book_view, registration_view, APIBookListView
from rest_framework.authtoken.views import obtain_auth_token

app_name = 'book'

urlpatterns = [
    path('item/<int:isbn>', api_detail_book_view, name='book-detail'),
    path('list/', APIBookListView.as_view(), name='book-list'),
    path('register/', registration_view, name='register'),
    path('login/', obtain_auth_token, name='login'),
]