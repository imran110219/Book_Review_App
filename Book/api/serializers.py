from rest_framework.serializers import (
    ModelSerializer,
    SerializerMethodField,
    HyperlinkedIdentityField,
    ListSerializer,
    PrimaryKeyRelatedField,
)
from django.db import transaction
from Book.models import Book, AuthorBook, BookCategory
from Author.models import Author
from Category.models import Category

from Author.api.serializers import AuthorListSerializer, AuthorDetailSerializer
from Category.api.serializers import CategoryListSerializer, CategoryDetailSerializer
from Publication.api.serializers import PublicationListSerializer

book_detail_url = HyperlinkedIdentityField(
    view_name='books-api:detail'
)


class BookCreateUpdateSerializer(ModelSerializer):
    authors = AuthorDetailSerializer(many=True, read_only=True)
    categories = CategoryDetailSerializer(many=True, read_only=True)

    @transaction.atomic
    def create(self, validated_data):
        book = Book.objects.create(**validated_data)

        if "authors" in self.initial_data:
            authors = self.initial_data.get("authors")
            for author in authors.split(","):
                author_instance = Author.objects.get(pk=int(author))
                AuthorBook(book=book, author=author_instance).save()

        if "categories" in self.initial_data:
            categories = self.initial_data.get("categories")
            for category in categories.split(","):
                category_instance = Category.objects.get(pk=int(category))
                BookCategory(book=book, category=category_instance).save()

        book.save()
        return book

    @transaction.atomic
    def update(self, instance, validated_data):
        # Ignore the fact that i delete and replace. Will diff in the future

        AuthorBook.objects.filter(book=instance).delete()
        authors = self.initial_data.get("authors")
        for author in authors.split(","):
            new_author = Author.objects.get(pk=int(author))
            AuthorBook(book=instance, author=new_author).save()

        BookCategory.objects.filter(book=instance).delete()
        categories = self.initial_data.get("categories")
        for category in categories.split(","):
            new_category = Category.objects.get(pk=int(category))
            BookCategory(book=instance, category=new_category).save()

        instance.__dict__.update(**validated_data)
        instance.save()
        return instance

    class Meta:
        model = Book
        fields = [
            'name',
            'description',
            'price',
            'edition',
            'no_of_page',
            'country',
            'publication',
            'authors',
            'categories',
        ]


class BookListSerializer(ModelSerializer):
    url = book_detail_url

    class Meta:
        model = Book
        fields = [
            'url',
            'id',
            'name',
            'publication',
            'authors',
            'categories',
        ]


class BookDetailSerializer(ModelSerializer):
    image = SerializerMethodField()
    publication = PublicationListSerializer(many=False, read_only=True)
    authors = AuthorListSerializer(many=True, read_only=True)
    categories = CategoryListSerializer(many=True, read_only=True)

    class Meta:
        model = Book
        fields = [
            'id',
            'name',
            'image',
            'description',
            'price',
            'edition',
            'no_of_page',
            'country',
            'publication',
            'authors',
            'categories',
        ]

    def get_image(self, obj):
        try:
            image = obj.image.url
        except:
            image = None
        return image
