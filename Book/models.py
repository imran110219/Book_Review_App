from django.db import models
from django.core.urlresolvers import reverse
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericRelation
from star_ratings.models import Rating

from Publication.models import Publication
from Category.models import Category
from Author.models import Author

# Create your models here.

class Book(models.Model):
  name = models.CharField(max_length=100)
  description = models.TextField(max_length=500)
  image = models.ImageField(height_field="height_field", width_field="width_field")
  height_field = models.IntegerField(default=255)
  width_field = models.IntegerField(default=255)
  price = models.FloatField()
  edition = models.CharField(max_length=100)
  no_of_page = models.IntegerField()
  country = models.CharField(max_length=50)
  publication = models.ForeignKey(Publication, on_delete=models.CASCADE)
  authors = models.ManyToManyField(Author, through='AuthorBook')
  categories = models.ManyToManyField(Category, through='BookCategory')
  ratings = GenericRelation(Rating, related_query_name='books')

  def __unicode__(self):
    return str(self.name)

  def __str__(self):
    return str(self.name)

  def get_absolute_url(self):
    return reverse("books:detail", kwargs={"id": self.id})

  @property
  def get_content_type(self):
    instance = self
    content_type = ContentType.objects.get_for_model(instance.__class__)
    return content_type

# Book.objects.filter(ratings__isnull=False).order_by('ratings__average')

class BookCategory(models.Model):
  book = models.ForeignKey(Book, on_delete=models.CASCADE, )
  category = models.ForeignKey(Category, on_delete=models.CASCADE)

  def __unicode__(self):
    return self.book.name + " " + self.category.name

class AuthorBook(models.Model):
  author = models.ForeignKey(Author, on_delete=models.CASCADE)
  book = models.ForeignKey(Book, on_delete=models.CASCADE)

  def __unicode__(self):
    return self.book.name + " " + self.author.name