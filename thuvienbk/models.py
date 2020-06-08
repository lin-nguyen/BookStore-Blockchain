from django.contrib.auth.models import AbstractUser
import datetime
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth import get_user_model
from django.conf import settings
from django.db import models
from PIL import Image
from django.utils import timezone

class CustomUser(AbstractUser):
    pass

    def __str__(self):
        return self.email


class UserProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} profile'

    def save(self, *args, **kwargs):
        super(UserProfile, self).save(*args, **kwargs)
        img = Image.open(self.image.path)
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)


class BookCategory(models.Model):
    category_name = models.CharField(max_length=50)


class BookAuthor(models.Model):
    author_name = models.CharField(max_length=50)


class Book(models.Model):
    title = models.CharField(max_length=100)
    authors = models.ManyToManyField(BookAuthor)
    language = models.CharField(max_length=50)
    publisher_name = models.CharField(max_length=50)
    published_year = models.IntegerField(default=0)
    ISBN = models.IntegerField(unique=True)
    categories = models.ManyToManyField(BookCategory)
    price = models.FloatField(default=0.0)
    rating_point = models.FloatField(default=0.0)
    num_of_rates = models.IntegerField(default=0)
    in_stocks = models.IntegerField(default=0)
    sales_volume = models.IntegerField(default=0)

    def __str__(self):
        return self.title


class BookImage(models.Model):
    book = models.OneToOneField(Book, on_delete=models.CASCADE)
    image = models.ImageField(default='book_default.jpg', upload_to='book_pics')


class BookPdf(models.Model):
    book = models.OneToOneField(Book, on_delete=models.CASCADE)
    book_pdf = models.FileField(upload_to='ebooks/')


class Transaction(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    book = models.OneToOneField(Book, on_delete=models.SET_NULL, null=True)
    start_time = models.DateTimeField(default=timezone.now)
    end_time = models.DateTimeField(default=timezone.now, null=True)
    state = models.IntegerField(default=0)
    description = models.TextField()


class PaymentMethod(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    wallet_address = models.CharField(max_length=100)
    private_key = models.CharField(max_length=100)

    def __str__(self):
        return self.wallet_address


class Rating(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    point = models.IntegerField(default=0, validators=[MaxValueValidator(5), MinValueValidator(1)])
    comment = models.CharField(max_length=100)


# class PhongThuVien(models.Model):
#     ma_so_phong = models.CharField(max_length=100,unique=True)
#     so_luong_sach_toi_da_co_the_chua= models.IntegerField(default=100)
#
# class NguoiQuanLyThuVien(models.Model):
#     user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
#     cmnd= models.CharField(max_length=200,unique=True)
#     ho_va_ten = models.CharField(max_length=200)
#     dob = models.DateField(blank=True, null=True)
#     gioi_tinh = models.CharField(max_length=3, choices=[('Nam','Nam'),('Nu','Nu')], default='Nam')
#     dia_chi_nha = models.CharField(max_length=300)
#     ma_so_quan_ly = models.CharField(max_length=100, unique=True)
#     phong_thu_vien_quan_ly = models.OneToOneField(PhongThuVien, on_delete=models.CASCADE)
#
# class ChuyenNganhSinhVien(models.Model):
#     ten_chuyen_nganh = models.CharField(max_length=100,unique=True)
#
# class SinhVien(models.Model):
#     user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
#     cmnd= models.CharField(max_length=200,unique=True)
#     ho_va_ten = models.CharField(max_length=200)
#     dob = models.DateField(blank=True, null=True)
#     gioi_tinh = models.CharField(max_length=3, choices=[('Nam','Nam'),('Nu','Nu')], default='Nam')
#     dia_chi_nha = models.CharField(max_length=300)
#
#     ma_so_sinh_vien = models.CharField(max_length=100, unique=True)
#     chuyen_nganh = models.ForeignKey(ChuyenNganhSinhVien, on_delete=models.CASCADE)
#
#     def sach_da_muon(self):
#         return SinhVienMuonSach.objects.filter(sinh_vien_id=self.id)
#
#     def sach_da_mua(self):
#         return SinhVienMuaSach.objects.filter(sinh_vien_id=self.id)
#
# class SinhVienMuaSach(models.Model):
#     sinh_vien = models.ForeignKey(SinhVien, on_delete=models.CASCADE)
#     sach= models.ForeignKey(Sach, on_delete=models.CASCADE)
#     ngay_mua = models.DateTimeField()
#
# class SinhVienMuonSach(models.Model):
#     sinh_vien = models.ForeignKey(SinhVien, on_delete=models.CASCADE)
#     sach= models.ForeignKey(Sach, on_delete=models.CASCADE)
#     ngay_muon = models.DateTimeField()
#     da_tra_sach = models.BooleanField(default=False)
#     ngay_tra_sach = models.DateField(blank=True, null=True)
#
# class DanhGiaSach(models.Model):
#     sinh_vien = models.ForeignKey(SinhVien, on_delete=models.CASCADE)
#     sach= models.ForeignKey(Sach, on_delete=models.CASCADE)
#     rating = models.IntegerField(default=0,validators=[MaxValueValidator(5), MinValueValidator(1)])
#     comment = models.CharField(max_length=100)
