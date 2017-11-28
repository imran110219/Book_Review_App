from django.db import models
from django.core.urlresolvers import reverse
from django.contrib.contenttypes.models import ContentType

from Publication.models import Publication
from Category.models import Category
from Author.models import Author

# Create your models here.

class Book(models.Model):
  book_name = models.CharField(max_length=100)
  book_description = models.TextField(max_length=500)
  book_image = models.ImageField(height_field="height_field", width_field="width_field")
  height_field = models.IntegerField(default=255)
  width_field = models.IntegerField(default=255)
  publication = models.ForeignKey(Publication, on_delete=models.CASCADE)
  authors = models.ManyToManyField(Author, through='AuthorBook')
  categories = models.ManyToManyField(Category, through='BookCategory')

  def __unicode__(self):
    return str(self.book_name)

  def __str__(self):
    return str(self.book_name)

  def get_absolute_url(self):
    return reverse("books:detail", kwargs={"id": self.id})

  @property
  def get_content_type(self):
    instance = self
    content_type = ContentType.objects.get_for_model(instance.__class__)
    return content_type

class BookCategory(models.Model):
  book = models.ForeignKey(Book, on_delete=models.CASCADE, )
  category = models.ForeignKey(Category, on_delete=models.CASCADE)

class AuthorBook(models.Model):
  author = models.ForeignKey(Author, on_delete=models.CASCADE)
  book = models.ForeignKey(Book, on_delete=models.CASCADE)