from django.core.management.base import BaseCommand, CommandError
import datetime
import random
from django.contrib.auth import get_user_model
from thuvienbk.models import UserProfile, BookCategory, BookAuthor, Book,\
	BookImage, BookPdf, Transaction, PaymentMethod, Rating


class Command(BaseCommand):

	def handle(self, *args, **options):

		User = get_user_model()
		Transaction.objects.all().delete()
		PaymentMethod.objects.all().delete()
		Rating.objects.all().delete()
		Book.objects.all().delete()
		BookCategory.objects.all().delete()
		BookAuthor.objects.all().delete()

		# User (10 users)
		user0 = User.objects.create_user(email='conganh1991999@gmail.com', password='fromBKU2017', username='anhnguyen')
		user0.save()
		user1 = User.objects.create_user(email='lehoanganh1999@gmail.com', password='fromBKU2018', username='hoanganh')
		user1.save()
		user2 = User.objects.create_user(email='baanh1999@gmail.com', password='fromBKU2019', username='baanh')
		user2.save()
		user3 = User.objects.create_user(email='tronganh1999@gmail.com', password='fromBKU2020', username='tronganh')
		user3.save()
		user4 = User.objects.create_user(email='ngocanh1999@gmail.com', password='fromBKU2021', username='ngocanh')
		user4.save()
		user5 = User.objects.create_user(email='tuananh1999@gmail.com', password='fromBKU2022', username='tuananh')
		user5.save()
		user6 = User.objects.create_user(email='thaibinh1999@gmail.com', password='fromBKU2023', username='binhnguyen')
		user6.save()
		user7 = User.objects.create_user(email='duyan1999@gmail.com', password='fromBKU2024', username='duyan')
		user7.save()
		user8 = User.objects.create_user(email='quoccuong1999@gmail.com', password='fromBKU2025', username='cuongnguyen')
		user8.save()
		user9 = User.objects.create_user(email='quangchinh1991999@gmail.com', password='fromBKU2026', username='chinhdoan')
		user9.save()

		# Book Categories
		category0 = BookCategory(category_name='Action and Adventure')
		category0.save()
		category1 = BookCategory(category_name='Anthology')
		category1.save()
		category2 = BookCategory(category_name='Classic')
		category2.save()
		category3 = BookCategory(category_name='Comic and Graphic Novel')
		category3.save()
		category4 = BookCategory(category_name='Drama')
		category4.save()
		category5 = BookCategory(category_name='Fairy Tale')
		category5.save()
		category6 = BookCategory(category_name='Fan-Fiction')
		category6.save()
		category7 = BookCategory(category_name='Historical Fiction')
		category7.save()
		category8 = BookCategory(category_name='Fantasy')
		category8.save()
		category9 = BookCategory(category_name='Horror')
		category9.save()
		category10 = BookCategory(category_name='Humor')
		category10.save()
		category11 = BookCategory(category_name='Legend')
		category11.save()
		category12 = BookCategory(category_name='Mystery')
		category12.save()
		category13 = BookCategory(category_name='Romance')
		category13.save()
		category14 = BookCategory(category_name='Realistic Fiction')
		category14.save()
		category15 = BookCategory(category_name='Short Story')
		category15.save()
		category16 = BookCategory(category_name='Science Fiction')
		category16.save()

		# Book Authors
		author0 = BookAuthor(author_name='Stephen King')
		author0.save()
		author1 = BookAuthor(author_name='Rick Riordan')
		author1.save()
		author2 = BookAuthor(author_name='Cassandra Clare')
		author2.save()
		author3 = BookAuthor(author_name='Neil Gaiman')
		author3.save()
		author4 = BookAuthor(author_name='John Green')
		author4.save()
		author5 = BookAuthor(author_name='James Patterson')
		author5.save()
		author6 = BookAuthor(author_name='Dan Brown')
		author6.save()
		author7 = BookAuthor(author_name='Nicholas Sparks')
		author7.save()
		author8 = BookAuthor(author_name='Veronica Roth')
		author8.save()
		author9 = BookAuthor(author_name='John Grisham')
		author9.save()
		author10 = BookAuthor(author_name='Nora Roberts')
		author10.save()
		author11 = BookAuthor(author_name='Sarah J. Maas')
		author11.save()
		author12 = BookAuthor(author_name='Gillian Flynn')
		author12.save()
		author13 = BookAuthor(author_name='Brandon Sanderson')
		author13.save()
		author14 = BookAuthor(author_name='Jodi Picoult')
		author14.save()

		# Books
		book0 = Book(title='Detective Conan chap 1', language='Japanese', publisher_name='Kim Dong', published_year=2000,
					 ISBN=97831614, price=12.0, rating_point=4.0, num_of_rates=98, in_stocks=120, sales_volume=160)
		book0.save()
		book0.authors.add(author1)
		book0.categories.add(category0)
		book0.categories.add(category1)

		book1 = Book(title='Detective Conan chap 2', language='Japanese', publisher_name='Kim Dong', published_year=2002,
					 ISBN=97831711, price=20.0, rating_point=4.5, num_of_rates=65, in_stocks=100, sales_volume=100)
		book1.save()
		book1.authors.add(author1)
		book1.categories.add(category0)
		book1.categories.add(category1)

		book2 = Book(title='Detective Conan chap 3', language='Japanese', publisher_name='Kim Dong', published_year=2002,
					 ISBN=97831944, price=22.0, rating_point=3.3, num_of_rates=40, in_stocks=60, sales_volume=92)
		book2.save()
		book2.authors.add(author1)
		book2.categories.add(category0)
		book2.categories.add(category1)

		book3 = Book(title='Harry Potter and the Philosopher\'s Stone', language='English', publisher_name='Penguin Random House',
					 published_year=1997, ISBN=97131415, price=15.0, rating_point=4.6, num_of_rates=106, in_stocks=400, sales_volume=260)
		book3.save()
		book3.authors.add(author6)
		book3.authors.add(author7)
		book3.categories.add(category4)

		book4 = Book(title='Harry Potter and the Cursed Child', language='English', publisher_name='Penguin Random House',
					 published_year=2000, ISBN=97831313, price=26.0, rating_point=4.8, num_of_rates=126, in_stocks=200, sales_volume=310)
		book4.save()
		book4.authors.add(author6)
		book4.authors.add(author7)
		book4.categories.add(category4)

		book5 = Book(title='Harry Potter and the Chamber of Secrets', language='English', publisher_name='Penguin Random House',
					 published_year=2006, ISBN=98135433, price=20.0, rating_point=4.2, num_of_rates=192, in_stocks=200, sales_volume=282)
		book5.save()
		book5.authors.add(author6)
		book5.authors.add(author7)
		book5.categories.add(category4)

		book6 = Book(title='War and Peace', language='English', publisher_name='HarperCollins', published_year=2012,
					 ISBN=99938164, price=7.5, rating_point=4.1, num_of_rates=46, in_stocks=80, sales_volume=120)
		book6.save()
		book6.authors.add(author8)
		book6.categories.add(category9)
		book6.categories.add(category1)
		book6.categories.add(category12)

		book7 = Book(title='Song of Solomon', language='English', publisher_name='Macmillan Publishers', published_year=2003,
					 ISBN=98031331, price=14.9, rating_point=3.6, num_of_rates=66, in_stocks=70, sales_volume=112)
		book7.save()
		book7.authors.add(author9)
		book7.authors.add(author10)
		book7.categories.add(category7)
		book7.categories.add(category13)

		book8 = Book(title='The Shadow of the Wind', language='English', publisher_name='Simon & Schuster', published_year=1999,
					 ISBN=97811111, price=16.9, rating_point=4.7, num_of_rates=32, in_stocks=100, sales_volume=178)
		book8.save()
		book8.authors.add(author11)
		book8.categories.add(category2)

		book9 = Book(title='The Lord of the Rings', language='English', publisher_name='Simon & Schuster', published_year=1999,
					 ISBN=97811112, price=13.0, rating_point=0.0, num_of_rates=0, in_stocks=30, sales_volume=0)
		book9.save()
		book9.authors.add(author13)
		book9.categories.add(category6)
		book9.categories.add(category12)
		book8.categories.add(category1)
		book8.categories.add(category15)

		# Payment Method
		payment_method00 = PaymentMethod(user=user1, wallet_address='Coinbase', private_key='1Tq3VlmnTScXlBXX')
		payment_method00.save()
		payment_method01 = PaymentMethod(user=user1, wallet_address='Ledger', private_key='FYQxnMIcLgoMDOeF')
		payment_method01.save()
		payment_method10 = PaymentMethod(user=user2, wallet_address='Coinbase', private_key='3BMXH5j6arBfujUf')
		payment_method10.save()
		payment_method11 = PaymentMethod(user=user2, wallet_address='Ledger', private_key='QmdAUAOFeiup2EOd')
		payment_method11.save()
		payment_method20 = PaymentMethod(user=user3, wallet_address='Coinbase', private_key='rlziOFGoSzlOunrq')
		payment_method20.save()
		payment_method21 = PaymentMethod(user=user3, wallet_address='Ledger', private_key='aU57YSiUINJ9eLm0')
		payment_method21.save()
		payment_method30 = PaymentMethod(user=user6, wallet_address='Coinbase', private_key='XiF5IJxZrZqrrD78')
		payment_method30.save()
		payment_method31 = PaymentMethod(user=user6, wallet_address='Ledger', private_key='LVXC3G3UGRwH6Lku')
		payment_method31.save()
		payment_method40 = PaymentMethod(user=user8, wallet_address='Coinbase', private_key='vk7WGQCfllpes0Hu')
		payment_method40.save()
		payment_method41 = PaymentMethod(user=user8, wallet_address='Ledger', private_key='X01lGKXNdXe2nFcB')
		payment_method41.save()

		# Transactions
		tran0 = Transaction(user=user0, book=book0, start_time='2000-10-25 14:30:59', end_time='2000-10-25 14:32:04',
							state=0, description='No description')
		tran0.save()
		tran1 = Transaction(user=user0, book=book1, start_time='2002-06-10 14:30:59', end_time='2002-06-10 14:32:04',
							state=1, description='No description')
		tran1.save()
		tran2 = Transaction(user=user0, book=book2, start_time='2002-10-25 14:30:59', end_time='2002-10-25 14:32:04',
							state=2, description='No description')
		tran2.save()
		tran3 = Transaction(user=user0, book=book3, start_time='1997-10-25 14:30:59', end_time='1997-10-25 14:32:04',
							state=2, description='No description')
		tran3.save()
		tran4 = Transaction(user=user0, book=book4, start_time='2000-04-15 14:30:59', end_time='2000-04-15 14:32:04',
							state=0, description='No description')
		tran4.save()
		tran5 = Transaction(user=user0, book=book5, start_time='2006-10-25 14:30:59', end_time='2006-10-25 14:32:04',
							state=0, description='No description')
		tran5.save()

		print('data inserted')
