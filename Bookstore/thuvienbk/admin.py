from django.contrib.auth.admin import UserAdmin
from django.contrib import admin
from django.contrib.auth import get_user_model
from django.utils.safestring import mark_safe
from .models import CustomUser, UserProfile, BookCategory, BookAuthor, Book, BookImage, Transaction, PaymentMethod, Rating
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


# class PhongThuVienAdmin(admin.ModelAdmin):
#     list_display = ('id','ma_so_phong', 'so_luong_sach_toi_da_co_the_chua')
#
#
# class NguoiQuanLyThuVienAdmin(admin.ModelAdmin):
#     list_display = ('id','ma_so_quan_ly','cmnd','ho_va_ten','dob','gioi_tinh','dia_chi_nha','phong_thu_vien_quan_ly')
#
#
# class ChuyenNganhSinhVienAdmin(admin.ModelAdmin):
#     list_display = ('id','ten_chuyen_nganh')
#
#
# class SinhVienAdmin(admin.ModelAdmin):
#     list_display = ('id','ma_so_sinh_vien','chuyen_nganh','cmnd','ho_va_ten','dob','gioi_tinh','dia_chi_nha')
#
#
# class SinhVienMuaSachAdmin(admin.ModelAdmin):
#     list_display = ('id','sinh_vien','sach','ngay_mua')
#
#
# class SinhVienMuonSachAdmin(admin.ModelAdmin):
#     list_display = ('id','sinh_vien','sach','ngay_muon','ngay_tra_sach', 'da_tra_sach')
#
#
# class DanhGiaSachAdmin(admin.ModelAdmin):
#     list_display = ('id','sinh_vien','sach','rating','comment')

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(UserProfile)
admin.site.register(BookAuthor, BookAuthorAdmin)
admin.site.register(BookCategory, BookCategoryAdmin)
admin.site.register(Book, BookAdmin)
admin.site.register(BookImage)
admin.site.register(Transaction)
admin.site.register(PaymentMethod)
admin.site.register(Rating)

# admin.site.register(SinhVienMuaSach, SinhVienMuaSachAdmin)
# admin.site.register(SinhVienMuonSach, SinhVienMuonSachAdmin)
# admin.site.register(DanhGiaSach, DanhGiaSachAdmin)
# admin.site.register(PhongThuVien, PhongThuVienAdmin)
# admin.site.register(NguoiQuanLyThuVien, NguoiQuanLyThuVienAdmin)
# admin.site.register(ChuyenNganhSinhVien, ChuyenNganhSinhVienAdmin)
# admin.site.register(SinhVien, SinhVienAdmin)