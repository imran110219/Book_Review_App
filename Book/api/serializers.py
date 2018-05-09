from rest_framework.serializers import (
    ModelSerializer,
    SerializerMethodField,
    HyperlinkedIdentityField,
    ListSerializer,
    PrimaryKeyRelatedField,
)
from django.db import transaction
from Book.models import Book, AuthorBook
from Author.models import Author

from Author.api.serializers import AuthorListSerializer, AuthorDetailSerializer
from Category.api.serializers import CategoryListSerializer, CategoryDetailSerializer
from Publication.api.serializers import PublicationListSerializer

book_detail_url = HyperlinkedIdentityField(
    view_name='books-api:detail'
)


class BookCreateUpdateSerializer(ModelSerializer):
    authors = AuthorDetailSerializer(many=True, read_only=True)
    categories = CategoryDetailSerializer(many=True, read_only=True)

    # def create(self, validated_data):
    #     temp_validated_data = validated_data
    #     if "authors" in validated_data:
    #         del validated_data["authors"]
    #     book = Book.objects.create(**validated_data)
    #     # for author in author_data:
    #     #   d = dict(author)
    #     #   AuthorBook.objects.create(book=book, author=d['author'])
    #     for attr, value in temp_validated_data.items():
    #         if str(attr) == 'authors':
    #             book.authors.add(value)
    #
    #     book.save()
    #     return book

    @transaction.atomic
    def create(self, validated_data):
        book = Book.objects.create(**validated_data)
        if "authors" in self.initial_data:
            authors = self.initial_data.get("authors")
            for author in authors.split(","):
                # id = author.get(id)
                author_instance = Author.objects.get(pk=int(author))
                AuthorBook(book=book, author=author_instance).save()
        book.save()
        return book

    def update(self, instance, validated_data):
        author_data = validated_data.pop('authors')
        for item in validated_data:
            if Book._meta.get_field(item):
                setattr(instance, item, validated_data[item])
                AuthorBook.objects.filter(book=instance).delete()
        for author in author_data:
            d = dict(author)
            AuthorBook.objects.create(book=instance, author=d['author'])
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
