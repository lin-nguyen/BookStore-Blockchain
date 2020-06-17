from django.contrib.auth.admin import UserAdmin
from django.contrib import admin
from django.contrib.auth import get_user_model
from django.utils.safestring import mark_safe
from .models import CustomUser, UserProfile, BookCategory, BookAuthor, Book, BookImage, BookPdf, Transaction, PaymentMethod, Rating
from .forms import CustomUserCreationForm, CustomUserChangeForm

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['email', 'username',]


class BookCategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'category_name',]


class BookAuthorAdmin(admin.ModelAdmin):
    list_display = ['author_name',]


class BookAdmin(admin.ModelAdmin):
    list_display = ['ISBN', 'title', 'language', 'publisher_name', 'published_year', 'price', 'rating_point', 'in_stocks', 'sales_volume',]

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(UserProfile)
admin.site.register(BookAuthor, BookAuthorAdmin)
admin.site.register(BookCategory, BookCategoryAdmin)
admin.site.register(Book, BookAdmin)
admin.site.register(BookImage)
admin.site.register(BookPdf)
admin.site.register(Transaction)
admin.site.register(PaymentMethod)
admin.site.register(Rating)
