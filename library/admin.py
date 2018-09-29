from django.contrib import admin

from library.models import Book

class BookAdmin(admin.ModelAdmin):
    list_display = ['title','price','pages']
    search_fields = ['title']
    list_filter = ['pages', 'price']
    fields = ['title','pages','price','isbn']

# Register your models here.
admin.site.register(Book, BookAdmin)
