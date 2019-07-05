from django.contrib import admin
from .models import Book, Word, Dictionary

# admin.site.register(Author)
admin.site.register(Book)
admin.site.register(Word)
admin.site.register(Dictionary)
# admin.site.register(Membership)