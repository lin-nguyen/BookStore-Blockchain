from django.core.management.base import BaseCommand, CommandError
from thuvienbk.models import  PhongThuVien, NguoiQuanLyThuVien,ChuyenNganhSinhVien,SinhVien,TheLoaiSach,Sach,SinhVienMuaSach,SinhVienMuonSach,DanhGiaSach
import datetime
import random
from django.contrib.auth import get_user_model


class Command(BaseCommand):

	def handle(self, *args, **options):

		User = get_user_model()
		PhongThuVien.objects.all().delete()
		NguoiQuanLyThuVien.objects.all().delete()
		ChuyenNganhSinhVien.objects.all().delete()
		SinhVien.objects.all().delete()
		TheLoaiSach.objects.all().delete()
		Sach.objects.all().delete()
		SinhVienMuaSach.objects.all().delete()
		SinhVienMuonSach.objects.all().delete()
		DanhGiaSach.objects.all().delete()

		#Phongthuvien (10 phong)
		p1=PhongThuVien(ma_so_phong='P101',so_luong_sach_toi_da_co_the_chua=100);
		p1.save();
		p2=PhongThuVien(ma_so_phong='P102',so_luong_sach_toi_da_co_the_chua=100);
		p2.save();
		p3=PhongThuVien(ma_so_phong='P103',so_luong_sach_toi_da_co_the_chua=100);
		p3.save();
		p4=PhongThuVien(ma_so_phong='P104',so_luong_sach_toi_da_co_the_chua=100);
		p4.save();
		p5=PhongThuVien(ma_so_phong='P105',so_luong_sach_toi_da_co_the_chua=100);
		p5.save();
		p6=PhongThuVien(ma_so_phong='P106',so_luong_sach_toi_da_co_the_chua=100);
		p6.save();
		p7=PhongThuVien(ma_so_phong='P107',so_luong_sach_toi_da_co_the_chua=100);
		p7.save();
		p8=PhongThuVien(ma_so_phong='P108',so_luong_sach_toi_da_co_the_chua=100);
		p8.save();
		p9=PhongThuVien(ma_so_phong='P109',so_luong_sach_toi_da_co_the_chua=100);
		p9.save();
		p10=PhongThuVien(ma_so_phong='P110',so_luong_sach_toi_da_co_the_chua=100);
		p10.save();

		#Quan ly thu vien (10 nguoi)
		quanly1=User.objects.create_user('quanly1', password='quanly1',email = 'quanly1@gmail.com',is_superuser=True,is_staff=True)
		quanly1=NguoiQuanLyThuVien(user=quanly1, ma_so_quan_ly='quanly1',cmnd='CMND-0000001',ho_va_ten='NGUYEN VAN A',dia_chi_nha='diachi1',dob='1929-05-07',gioi_tinh='Nam',phong_thu_vien_quan_ly=p1); quanly1.save()

		quanly2=User.objects.create_user('quanly2', password='quanly2',email = 'quanly2@gmail.com',is_superuser=True,is_staff=True)
		quanly2=NguoiQuanLyThuVien(user=quanly2, ma_so_quan_ly='quanly2',cmnd='CMND-0000002',ho_va_ten='NGUYEN VAN B',dia_chi_nha='diachi2',dob='1929-05-08',gioi_tinh='Nam',phong_thu_vien_quan_ly=p2); quanly2.save()

		quanly3=User.objects.create_user('quanly3', password='quanly3',email = 'quanly3@gmail.com',is_superuser=True,is_staff=True)
		quanly3=NguoiQuanLyThuVien(user=quanly3, ma_so_quan_ly='quanly3',cmnd='CMND-0000003',ho_va_ten='NGUYEN VAN C',dia_chi_nha='diachi3',dob='1929-05-09',gioi_tinh='Nu',phong_thu_vien_quan_ly=p3); quanly3.save()

		quanly4=User.objects.create_user('quanly4', password='quanly4',email = 'quanly4@gmail.com',is_superuser=True,is_staff=True)
		quanly4=NguoiQuanLyThuVien(user=quanly4, ma_so_quan_ly='quanly4',cmnd='CMND-0000004',ho_va_ten='NGUYEN VAN D',dia_chi_nha='diachi4',dob='1929-06-07',gioi_tinh='Nu',phong_thu_vien_quan_ly=p4); quanly4.save()

		quanly5=User.objects.create_user('quanly5', password='quanly5',email = 'quanly5@gmail.com',is_superuser=True,is_staff=True)
		quanly5=NguoiQuanLyThuVien(user=quanly5, ma_so_quan_ly='quanly5',cmnd='CMND-0000005',ho_va_ten='NGUYEN VAN E',dia_chi_nha='diachi5',dob='1922-05-07',gioi_tinh='Nu',phong_thu_vien_quan_ly=p5); quanly5.save()

		quanly6=User.objects.create_user('quanly6', password='quanly6',email = 'quanly6@gmail.com',is_superuser=True,is_staff=True)
		quanly6=NguoiQuanLyThuVien(user=quanly6, ma_so_quan_ly='quanly6',cmnd='CMND-0000006',ho_va_ten='NGUYEN VAN F',dia_chi_nha='diachi6',dob='1925-05-07',gioi_tinh='Nu',phong_thu_vien_quan_ly=p6); quanly6.save()

		quanly7=User.objects.create_user('quanly7', password='quanly7',email = 'quanly7@gmail.com',is_superuser=True,is_staff=True)
		quanly7=NguoiQuanLyThuVien(user=quanly7, ma_so_quan_ly='quanly7',cmnd='CMND-0000007',ho_va_ten='NGUYEN VAN G',dia_chi_nha='diachi7',dob='1926-05-07',gioi_tinh='Nu',phong_thu_vien_quan_ly=p7); quanly7.save()

		quanly8=User.objects.create_user('quanly8', password='quanly8',email = 'quanly8@gmail.com',is_superuser=True,is_staff=True)
		quanly8=NguoiQuanLyThuVien(user=quanly8, ma_so_quan_ly='quanly8',cmnd='CMND-0000008',ho_va_ten='NGUYEN VAN H',dia_chi_nha='diachi8',dob='1927-06-07',gioi_tinh='Nu',phong_thu_vien_quan_ly=p8); quanly8.save()

		quanly9=User.objects.create_user('quanly9', password='quanly9',email = 'quanly9@gmail.com',is_superuser=True,is_staff=True)
		quanly9=NguoiQuanLyThuVien(user=quanly9, ma_so_quan_ly='quanly9',cmnd='CMND-0000009',ho_va_ten='NGUYEN VAN I',dia_chi_nha='diachi9',dob='1956-08-07',gioi_tinh='Nam',phong_thu_vien_quan_ly=p9); quanly9.save()

		quanly10=User.objects.create_user('quanly10', password='quanly10',email = 'quanly10@gmail.com',is_superuser=True,is_staff=True)
		quanly10=NguoiQuanLyThuVien(user=quanly10, ma_so_quan_ly='quanly10	',cmnd='CMND-0000010',ho_va_ten='NGUYEN VAN J',dia_chi_nha='diachi10',dob='1951-05-01',gioi_tinh='Nam',phong_thu_vien_quan_ly=p10); quanly10.save()

		#Chuyen nganh sinh vien (10 chuyen nganh)
		cn1=ChuyenNganhSinhVien(ten_chuyen_nganh='CS'); cn1.save();
		cn2=ChuyenNganhSinhVien(ten_chuyen_nganh='PM'); cn2.save();
		cn3=ChuyenNganhSinhVien(ten_chuyen_nganh='DDT'); cn3.save();
		cn4=ChuyenNganhSinhVien(ten_chuyen_nganh='CK'); cn4.save();
		cn5=ChuyenNganhSinhVien(ten_chuyen_nganh='MT'); cn5.save();
		cn6=ChuyenNganhSinhVien(ten_chuyen_nganh='XD'); cn6.save();
		cn7=ChuyenNganhSinhVien(ten_chuyen_nganh='HOA'); cn7.save();
		cn8=ChuyenNganhSinhVien(ten_chuyen_nganh='DC'); cn8.save();
		cn9=ChuyenNganhSinhVien(ten_chuyen_nganh='NH'); cn9.save();
		cn10=ChuyenNganhSinhVien(ten_chuyen_nganh='CE'); cn10.save();


		#Sinh vien (20 sinh vien)
		sv1=User.objects.create_user('sv1', password='sv1',email = 'sv1@gmail.com')
		sv1=SinhVien(user=sv1, ma_so_sinh_vien='sv1',cmnd='CMND-1000001',ho_va_ten='TRAN VAN A',dia_chi_nha='KTX DHBK',dob='1996-05-06',gioi_tinh='Nu',chuyen_nganh=cn1); sv1.save()

		sv2=User.objects.create_user('sv2', password='sv2',email = 'sv2@gmail.com')
		sv2=SinhVien(user=sv2, ma_so_sinh_vien='sv2',cmnd='CMND-1000002',ho_va_ten='TRAN VAN B',dia_chi_nha='KTX DHBK',dob='1997-05-01',gioi_tinh='Nu',chuyen_nganh=cn1); sv2.save()

		sv3=User.objects.create_user('sv3', password='sv3',email = 'sv3@gmail.com')
		sv3=SinhVien(user=sv3, ma_so_sinh_vien='sv3',cmnd='CMND-1000003',ho_va_ten='TRAN VAN C',dia_chi_nha='KTX DHBK',dob='1996-05-02',gioi_tinh='Nu',chuyen_nganh=cn2); sv3.save()

		sv4=User.objects.create_user('sv4', password='sv4',email = 'sv4@gmail.com')
		sv4=SinhVien(user=sv4, ma_so_sinh_vien='sv4',cmnd='CMND-1000004',ho_va_ten='TRAN VAN D',dia_chi_nha='KTX DHBK',dob='1996-05-03',gioi_tinh='Nu',chuyen_nganh=cn2); sv4.save()

		sv5=User.objects.create_user('sv5', password='sv5',email = 'sv5@gmail.com')
		sv5=SinhVien(user=sv5, ma_so_sinh_vien='sv5',cmnd='CMND-1000005',ho_va_ten='TRAN VAN E',dia_chi_nha='KTX DHBK',dob='1996-05-05',gioi_tinh='Nam',chuyen_nganh=cn3); sv5.save()

		sv6=User.objects.create_user('sv6', password='sv6',email = 'sv6@gmail.com')
		sv6=SinhVien(user=sv6, ma_so_sinh_vien='sv6',cmnd='CMND-1000006',ho_va_ten='TRAN VAN F',dia_chi_nha='KTX DHBK',dob='1996-05-08',gioi_tinh='Nam',chuyen_nganh=cn3); sv6.save()

		sv7=User.objects.create_user('sv7', password='sv7',email = 'sv7@gmail.com')
		sv7=SinhVien(user=sv7, ma_so_sinh_vien='sv7',cmnd='CMND-1000007',ho_va_ten='TRAN VAN G',dia_chi_nha='KTX DHBK',dob='1995-01-07',gioi_tinh='Nam',chuyen_nganh=cn4); sv7.save()

		sv8=User.objects.create_user('sv8', password='sv8',email = 'sv8@gmail.com')
		sv8=SinhVien(user=sv8, ma_so_sinh_vien='sv8',cmnd='CMND-1000008',ho_va_ten='TRAN VAN H',dia_chi_nha='KTX DHBK',dob='1995-03-07',gioi_tinh='Nam',chuyen_nganh=cn4); sv8.save()

		sv9=User.objects.create_user('sv9', password='sv9',email = 'sv9@gmail.com')
		sv9=SinhVien(user=sv9, ma_so_sinh_vien='sv9',cmnd='CMND-1000009',ho_va_ten='TRAN VAN I',dia_chi_nha='KTX DHBK',dob='1995-07-07',gioi_tinh='Nu',chuyen_nganh=cn5); sv9.save()

		sv10=User.objects.create_user('sv10', password='sv10',email = 'sv10@gmail.com')
		sv10=SinhVien(user=sv10, ma_so_sinh_vien='sv10',cmnd='CMND-1000010',ho_va_ten='TRAN VAN J',dia_chi_nha='KTX DHBK',dob='1995-08-07',gioi_tinh='Nu',chuyen_nganh=cn5); sv10.save()

		sv11=User.objects.create_user('sv11', password='sv11',email = 'sv11@gmail.com')
		sv11=SinhVien(user=sv11, ma_so_sinh_vien='sv11',cmnd='CMND-1000011',ho_va_ten='TRAN VAN K',dia_chi_nha='KTX DHBK',dob='1995-09-07',gioi_tinh='Nu',chuyen_nganh=cn6); sv11.save()

		sv12=User.objects.create_user('sv12', password='sv12',email = 'sv12gmail.com')
		sv12=SinhVien(user=sv12, ma_so_sinh_vien='sv12',cmnd='CMND-1000012',ho_va_ten='TRAN VAN L',dia_chi_nha='KTX DHBK',dob='1998-10-07',gioi_tinh='Nam',chuyen_nganh=cn6); sv12.save()

		sv13=User.objects.create_user('sv13', password='sv13',email = 'sv13@gmail.com')
		sv13=SinhVien(user=sv13, ma_so_sinh_vien='sv13',cmnd='CMND-1000013',ho_va_ten='TRAN VAN M',dia_chi_nha='KTX DHBK',dob='1998-11-07',gioi_tinh='Nam',chuyen_nganh=cn7); sv13.save()

		sv14=User.objects.create_user('sv14', password='sv14',email = 'sv14@gmail.com')
		sv14=SinhVien(user=sv14, ma_so_sinh_vien='sv14',cmnd='CMND-1000014',ho_va_ten='TRAN VAN N',dia_chi_nha='KTX DHBK',dob='1998-12-07',gioi_tinh='Nam',chuyen_nganh=cn7); sv14.save()

		sv15=User.objects.create_user('sv15', password='sv15',email = 'sv15@gmail.com')
		sv15=SinhVien(user=sv15, ma_so_sinh_vien='sv15',cmnd='CMND-1000015',ho_va_ten='TRAN VAN O',dia_chi_nha='Q10 Tp.HCM',dob='1998-07-07',gioi_tinh='Nam',chuyen_nganh=cn8); sv15.save()

		sv16=User.objects.create_user('sv16', password='sv16',email = 'sv16@gmail.com')
		sv16=SinhVien(user=sv16, ma_so_sinh_vien='sv16',cmnd='CMND-1000016',ho_va_ten='TRAN VAN P',dia_chi_nha='Q10 Tp.HCM',dob='1998-05-08',gioi_tinh='Nam',chuyen_nganh=cn8); sv16.save()

		sv17=User.objects.create_user('sv17', password='sv17',email = 'sv17@gmail.com')
		sv17=SinhVien(user=sv17, ma_so_sinh_vien='sv17',cmnd='CMND-1000017',ho_va_ten='TRAN VAN Q',dia_chi_nha='Q10 Tp.HCM',dob='1998-06-07',gioi_tinh='Nam',chuyen_nganh=cn9); sv17.save()

		sv18=User.objects.create_user('sv18', password='sv18',email = 'sv18@gmail.com')
		sv18=SinhVien(user=sv18, ma_so_sinh_vien='sv18',cmnd='CMND-1000018',ho_va_ten='TRAN VAN R',dia_chi_nha='Q10 Tp.HCM',dob='1998-01-07',gioi_tinh='Nam',chuyen_nganh=cn9); sv18.save()

		sv19=User.objects.create_user('sv19', password='sv19',email = 'sv19@gmail.com')
		sv19=SinhVien(user=sv19, ma_so_sinh_vien='sv19',cmnd='CMND-1000019',ho_va_ten='TRAN VAN W',dia_chi_nha='Q10 Tp.HCM',dob='1998-02-07',gioi_tinh='Nam',chuyen_nganh=cn10); sv19.save()

		sv20=User.objects.create_user('sv20', password='sv20',email = 'sv20@gmail.com')
		sv20=SinhVien(user=sv20, ma_so_sinh_vien='sv20',cmnd='CMND-1000020',ho_va_ten='TRAN VAN Y',dia_chi_nha='Q10 Tp.HCM',dob='1998-03-11',gioi_tinh='Nu',chuyen_nganh=cn10); sv20.save()

		sv21=User.objects.create_user('User', password='user',email = 'user@gmail.com')
		sv21=SinhVien(user=sv21, ma_so_sinh_vien='sv21',cmnd='CMND-1000021',ho_va_ten='TRAN VAN Na',dia_chi_nha='KTX DHBK',dob='1998-12-07',gioi_tinh='Nam',chuyen_nganh=cn7); sv21.save()

		#The loai sach (15 the loai)
		tl1=TheLoaiSach(the_loai_sach='Science');   tl1.save()
		tl2=TheLoaiSach(the_loai_sach='Nghe thuat'); tl2.save()
		tl3=TheLoaiSach(the_loai_sach='Dia ly');   tl3.save()
		tl4=TheLoaiSach(the_loai_sach='Toan tin');   tl4.save()
		tl5=TheLoaiSach(the_loai_sach='My Thuat');   tl5.save()
		tl6=TheLoaiSach(the_loai_sach='Xa Hoi');   tl6.save()
		tl7=TheLoaiSach(the_loai_sach='GDCD');   tl7.save()
		tl8=TheLoaiSach(the_loai_sach='My thuat');   tl8.save()
		tl9=TheLoaiSach(the_loai_sach='Vat ly');   tl9.save()
		tl10=TheLoaiSach(the_loai_sach='Cong nghe');   tl10.save()
		tl11=TheLoaiSach(the_loai_sach='Trinh tham');   tl11.save()
		tl12=TheLoaiSach(the_loai_sach='Tieu thuyet'); tl12.save()
		tl13=TheLoaiSach(the_loai_sach='Thieu nhi');   tl13.save()
		tl14=TheLoaiSach(the_loai_sach='Kinh di');   tl14.save()
		tl15=TheLoaiSach(the_loai_sach='Phieu luu');   tl15.save()



		#Sach ( 20 cuon )
		sach1=Sach(1,ten_sach='Toan cao cap',tac_gia='tac gia 1',nam_xuat_ban='1999',the_loai=tl1,gia_ban='10000',so_luong_ton_kho=10,so_luong_da_cho_muon=2,so_luong_da_ban=2); sach1.save()
		sach2=Sach(2,ten_sach='Ve tranh',tac_gia='tac gia 2',nam_xuat_ban='1999',the_loai=tl2,gia_ban='15000',so_luong_ton_kho=5, so_luong_da_cho_muon=2,so_luong_da_ban=2); sach2.save()
		sach3=Sach(3,ten_sach='Conan',tac_gia='tac gia 3',nam_xuat_ban='1999',the_loai=tl3,gia_ban='16000',so_luong_ton_kho=10,so_luong_da_cho_muon=2,so_luong_da_ban=24); sach3.save()
		sach4=Sach(4,ten_sach='One punch man',tac_gia='tac gia 4',nam_xuat_ban='2000',the_loai=tl4,gia_ban='17000',so_luong_ton_kho=20,so_luong_da_cho_muon=5,so_luong_da_ban=52); sach4.save()
		sach5=Sach(5,ten_sach='Vat ly',tac_gia='tac gia 5',nam_xuat_ban='1999',the_loai=tl5,gia_ban='18000',so_luong_ton_kho=30,so_luong_da_cho_muon=6,so_luong_da_ban=62); sach5.save()
		sach6=Sach(6,ten_sach='Hoa Hoc',tac_gia='tac gia 6',nam_xuat_ban='2000',the_loai=tl6,gia_ban='20000',so_luong_ton_kho=25,so_luong_da_cho_muon=12,so_luong_da_ban=60); sach6.save()
		sach7=Sach(7,ten_sach='Sinh Hoc',tac_gia='tac gia 6',nam_xuat_ban='2000',the_loai=tl7,gia_ban='21000',so_luong_ton_kho=45,so_luong_da_cho_muon=22,so_luong_da_ban=12); sach7.save()
		sach8=Sach(8,ten_sach='GDCD',tac_gia='tac gia 8',nam_xuat_ban='1999',the_loai=tl8,gia_ban='220000',so_luong_ton_kho=35,so_luong_da_cho_muon=21,so_luong_da_ban=55); sach8.save()
		sach9=Sach(9,ten_sach='Mac-Lenin',tac_gia='tac gia 9',nam_xuat_ban='1998',the_loai=tl9,gia_ban='30000',so_luong_ton_kho=50,so_luong_da_cho_muon=27,so_luong_da_ban=56); sach9.save()
		sach10=Sach(10,ten_sach='Lich su',tac_gia='tac gia 10',nam_xuat_ban='2001',the_loai=tl10,gia_ban='35000',so_luong_ton_kho=6,so_luong_da_cho_muon=48,so_luong_da_ban=200); sach10.save()

		sach11=Sach(11,ten_sach='Hero academy',tac_gia='tac gia 1',nam_xuat_ban='1999',the_loai=tl11,gia_ban='100000',so_luong_ton_kho=10,so_luong_da_cho_muon=5,so_luong_da_ban=29); sach11.save()
		sach12=Sach(12,ten_sach='Brawling',tac_gia='tac gia 2',nam_xuat_ban='2005',the_loai=tl12,gia_ban='13500',so_luong_ton_kho=15, so_luong_da_cho_muon=23,so_luong_da_ban=67); sach12.save()
		sach13=Sach(13,ten_sach='Hera',tac_gia='tac gia 3',nam_xuat_ban='2005',the_loai=tl13,gia_ban='26000',so_luong_ton_kho=10,so_luong_da_cho_muon=10,so_luong_da_ban=24); sach13.save()
		sach14=Sach(14,ten_sach='QTV',tac_gia='tac gia 4',nam_xuat_ban='2000',the_loai=tl14,gia_ban='37000',so_luong_ton_kho=20,so_luong_da_cho_muon=21,so_luong_da_ban=52); sach14.save()
		sach15=Sach(15,ten_sach='Zeros',tac_gia='tac gia 5',nam_xuat_ban='2010',the_loai=tl15,gia_ban='48000',so_luong_ton_kho=29,so_luong_da_cho_muon=13,so_luong_da_ban=62); sach15.save()
		sach16=Sach(16,ten_sach='Thay giao ba',tac_gia='tac gia 6',nam_xuat_ban='2009',the_loai=tl11,gia_ban='9000',so_luong_ton_kho=24,so_luong_da_cho_muon=17,so_luong_da_ban=60); sach16.save()
		sach17=Sach(17,ten_sach='Sena',tac_gia='tac gia 6',nam_xuat_ban='2008',the_loai=tl12,gia_ban='120000',so_luong_ton_kho=43,so_luong_da_cho_muon=25,so_luong_da_ban=12); sach17.save()
		sach18=Sach(18,ten_sach='Messi',tac_gia='tac gia 8',nam_xuat_ban='2007',the_loai=tl13,gia_ban='220000',so_luong_ton_kho=41,so_luong_da_cho_muon=26,so_luong_da_ban=55, dang_hot=True); sach18.save()
		sach19=Sach(19,ten_sach='Ronaldo',tac_gia='tac gia 9',nam_xuat_ban='2006',the_loai=tl14,gia_ban='33000',so_luong_ton_kho=55,so_luong_da_cho_muon=32,so_luong_da_ban=56, dang_hot=True); sach19.save()
		sach20=Sach(20,ten_sach='New Advanture',tac_gia='Travor James',nam_xuat_ban='11452',the_loai=tl1,gia_ban='10',so_luong_ton_kho=0,so_luong_da_cho_muon=10,so_luong_da_ban=500, dang_hot=True); sach20.save()


		#Sinh vien mua sach
		sv_mua_sach_1=SinhVienMuaSach(sinh_vien=sv1,sach=sach1,ngay_mua='2010-01-01'); sv_mua_sach_1.save();
		sv_mua_sach_2=SinhVienMuaSach(sinh_vien=sv2,sach=sach2,ngay_mua='2010-01-02'); sv_mua_sach_2.save();
		sv_mua_sach_3=SinhVienMuaSach(sinh_vien=sv3,sach=sach3,ngay_mua='2010-01-03'); sv_mua_sach_3.save();
		sv_mua_sach_4=SinhVienMuaSach(sinh_vien=sv4,sach=sach4,ngay_mua='2010-01-04'); sv_mua_sach_4.save();
		sv_mua_sach_5=SinhVienMuaSach(sinh_vien=sv5,sach=sach5,ngay_mua='2010-01-05'); sv_mua_sach_5.save();
		sv_mua_sach_6=SinhVienMuaSach(sinh_vien=sv6,sach=sach6,ngay_mua='2010-01-06'); sv_mua_sach_6.save();
		sv_mua_sach_7=SinhVienMuaSach(sinh_vien=sv7,sach=sach7,ngay_mua='2010-01-07'); sv_mua_sach_7.save();
		sv_mua_sach_8=SinhVienMuaSach(sinh_vien=sv8,sach=sach8,ngay_mua='2010-01-08'); sv_mua_sach_8.save();
		sv_mua_sach_9=SinhVienMuaSach(sinh_vien=sv9,sach=sach9,ngay_mua='2010-01-09'); sv_mua_sach_9.save();
		sv_mua_sach_10=SinhVienMuaSach(sinh_vien=sv10,sach=sach10,ngay_mua='2010-01-10'); sv_mua_sach_10.save();
		temp=SinhVienMuaSach(sinh_vien=sv10,sach=sach6,ngay_mua='2010-01-10'); temp.save();
		temp=SinhVienMuaSach(sinh_vien=sv10,sach=sach7,ngay_mua='2010-01-10'); temp.save();
		temp=SinhVienMuaSach(sinh_vien=sv21,sach=sach20,ngay_mua='2019-04-08'); temp.save();
		sv_mua_sach_11=SinhVienMuaSach(sinh_vien=sv11,sach=sach1,ngay_mua='2010-01-10'); sv_mua_sach_11.save();
		temp=SinhVienMuaSach(sinh_vien=sv11,sach=sach2,ngay_mua='2010-01-10'); temp.save();
		temp=SinhVienMuaSach(sinh_vien=sv11,sach=sach3,ngay_mua='2010-01-10'); temp.save();

		#Sinh vien muon sach
		sv_muon_sach_10=SinhVienMuonSach(sinh_vien=sv10,sach=sach4,ngay_muon='2010-01-11'); sv_muon_sach_10.save();
		temp=SinhVienMuonSach(sinh_vien=sv10,sach=sach5,ngay_muon='2010-01-11'); temp.save();
		temp=SinhVienMuonSach(sinh_vien=sv10,sach=sach6,ngay_muon='2010-01-11'); temp.save();
		sv_muon_sach_11=SinhVienMuonSach(sinh_vien=sv11,sach=sach11,ngay_muon='2010-01-11'); sv_muon_sach_11.save();
		temp=SinhVienMuonSach(sinh_vien=sv11,sach=sach4,ngay_muon='2010-01-11'); temp.save();
		temp=SinhVienMuonSach(sinh_vien=sv11,sach=sach5,ngay_muon='2010-01-11'); temp.save();

		sv_muon_sach_12=SinhVienMuonSach(sinh_vien=sv12,sach=sach12,ngay_muon='2010-01-12'); sv_muon_sach_12.save();
		sv_muon_sach_13=SinhVienMuonSach(sinh_vien=sv13,sach=sach13,ngay_muon='2010-01-13'); sv_muon_sach_13.save();
		sv_muon_sach_14=SinhVienMuonSach(sinh_vien=sv14,sach=sach14,ngay_muon='2010-01-14'); sv_muon_sach_14.save();
		sv_muon_sach_15=SinhVienMuonSach(sinh_vien=sv15,sach=sach15,ngay_muon='2010-01-15'); sv_muon_sach_15.save();
		sv_muon_sach_16=SinhVienMuonSach(sinh_vien=sv16,sach=sach16,ngay_muon='2010-01-16'); sv_muon_sach_16.save();
		sv_muon_sach_17=SinhVienMuonSach(sinh_vien=sv17,sach=sach17,ngay_muon='2010-01-17'); sv_muon_sach_17.save();
		sv_muon_sach_18=SinhVienMuonSach(sinh_vien=sv18,sach=sach18,ngay_muon='2010-01-18'); sv_muon_sach_18.save();
		sv_muon_sach_19=SinhVienMuonSach(sinh_vien=sv19,sach=sach19,ngay_muon='2010-01-19'); sv_muon_sach_19.save();
		sv_muon_sach_20=SinhVienMuonSach(sinh_vien=sv20,sach=sach20,ngay_muon='2010-01-20'); sv_muon_sach_20.save();

		# rating (1->5) comment ( ? )
		danh_gia_sach1=DanhGiaSach(sinh_vien=sv1,sach=sach1,rating=4,comment='comment1'); danh_gia_sach1.save();
		danh_gia_sach2=DanhGiaSach(sinh_vien=sv2,sach=sach2,rating=5,comment='comment2'); danh_gia_sach2.save();
		danh_gia_sach3=DanhGiaSach(sinh_vien=sv3,sach=sach3,rating=3,comment='comment3'); danh_gia_sach3.save();
		danh_gia_sach4=DanhGiaSach(sinh_vien=sv4,sach=sach4,rating=4,comment='comment4'); danh_gia_sach4.save();
		danh_gia_sach5=DanhGiaSach(sinh_vien=sv5,sach=sach5,rating=5,comment='comment5'); danh_gia_sach5.save();
		danh_gia_sach6=DanhGiaSach(sinh_vien=sv6,sach=sach6,rating=1,comment='comment6'); danh_gia_sach6.save();
		danh_gia_sach7=DanhGiaSach(sinh_vien=sv7,sach=sach7,rating=2,comment='comment7'); danh_gia_sach7.save();
		danh_gia_sach8=DanhGiaSach(sinh_vien=sv8,sach=sach8,rating=3,comment='comment8'); danh_gia_sach8.save();
		danh_gia_sach9=DanhGiaSach(sinh_vien=sv9,sach=sach9,rating=2,comment='comment9'); danh_gia_sach9.save();
		danh_gia_sach10=DanhGiaSach(sinh_vien=sv10,sach=sach10,rating=2,comment='comment10'); danh_gia_sach10.save();
		danh_gia_sach11=DanhGiaSach(sinh_vien=sv11,sach=sach11,rating=5,comment='comment11'); danh_gia_sach11.save();
		danh_gia_sach12=DanhGiaSach(sinh_vien=sv12,sach=sach12,rating=6,comment='comment12'); danh_gia_sach12.save();
		danh_gia_sach13=DanhGiaSach(sinh_vien=sv13,sach=sach13,rating=6,comment='comment13'); danh_gia_sach13.save();
		danh_gia_sach14=DanhGiaSach(sinh_vien=sv14,sach=sach14,rating=4,comment='comment14'); danh_gia_sach14.save();
		danh_gia_sach15=DanhGiaSach(sinh_vien=sv15,sach=sach15,rating=4,comment='comment15'); danh_gia_sach15.save();
		danh_gia_sach16=DanhGiaSach(sinh_vien=sv16,sach=sach16,rating=4,comment='comment16'); danh_gia_sach16.save();
		danh_gia_sach17=DanhGiaSach(sinh_vien=sv17,sach=sach17,rating=3,comment='comment17'); danh_gia_sach17.save();
		danh_gia_sach18=DanhGiaSach(sinh_vien=sv18,sach=sach18,rating=3,comment='comment18'); danh_gia_sach18.save();
		danh_gia_sach19=DanhGiaSach(sinh_vien=sv19,sach=sach19,rating=2,comment='comment19'); danh_gia_sach19.save();
		danh_gia_sach20=DanhGiaSach(sinh_vien=sv20,sach=sach20,rating=2,comment='comment20'); danh_gia_sach20.save();

		print('data inserted')
