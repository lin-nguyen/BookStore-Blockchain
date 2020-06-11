from rest_framework import serializers
from thuvienbk.models import Book, CustomUser

class BookSerializer(serializers.ModelSerializer):

    authors = serializers.SerializerMethodField('get_author_names')
    image = serializers.SerializerMethodField('get_image')

    class Meta:
        model = Book
        fields = ['ISBN', 'title', 'image', 'authors', 'price', 'published_year', 'language', 'in_stocks',
                  'rating_point', 'num_of_rates', 'in_stocks', 'sales_volume']

    def get_author_names(self, book):
        author_names = []
        for author in book.authors.all():
            author_names.append(author.author_name)
        return author_names

    def get_image(self, book):
        return book.bookimage.image.url


class RegisterSerializer(serializers.ModelSerializer):

    password2 = serializers.CharField(style={'input_type': 'password'}, write_only=True)

    class Meta:
        model = CustomUser
        fields = ['email', 'username', 'password', 'password2']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def save(self):
        user = CustomUser(
            email=self.validated_data['email'],
            username=self.validated_data['username'],
        )
        password = self.validated_data['password']
        password2 = self.validated_data['password2']

        if password != password2:
            raise serializers.ValidationError({'password': 'Password must match'})
        user.set_password(password)
        user.save()
        return user
