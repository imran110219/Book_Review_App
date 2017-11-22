from django.contrib import admin
from .models import Book, BookCategory, AuthorBook


# Register your models here.
class BookCategoryAdminInline(admin.TabularInline):
  model = BookCategory
  extra = 1


class BookAutorAdminInline(admin.TabularInline):
  model = AuthorBook
  extra = 1


class BookAdmin(admin.ModelAdmin):
  inlines = (BookCategoryAdminInline, BookAutorAdminInline)


class BookCategoryModelAdmin(admin.ModelAdmin):
  list_display = ["book", "category"]

  class meta:
    model = BookCategory


class AuthorBookModelAdmin(admin.ModelAdmin):
  list_display = ["author", "book"]

  class meta:
    model = AuthorBook


# class BookAdmin(admin.ModelAdmin):
#   model = Book
#   filter_horizontal = ('authors',)  # If you don't specify this, you will get a multiple select widget.


# admin.site.register(Author)
admin.site.register(Book, BookAdmin)

# admin.site.register(Book)
admin.site.register(BookCategory, BookCategoryModelAdmin)
admin.site.register(AuthorBook, AuthorBookModelAdmin)
