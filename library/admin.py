from django.contrib import admin

from library.models import Book, PublicationHouse, Review

class ReviewAdmin(admin.TabularInline):
    model = Review
    extra = 0

class BookAdmin(admin.ModelAdmin):
    list_display = ['title','price','pages']
    search_fields = ['title']
    list_filter = ['pages', 'price']
    fields = ['title','pages','price','isbn','publicationhouse']
    inlines = [ReviewAdmin]

# Register your models here.
admin.site.register(Book, BookAdmin)
# admin.site.register(Book)
admin.site.register(PublicationHouse)
