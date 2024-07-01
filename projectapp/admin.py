from django.contrib import admin

# Register your models here.
from projectapp.models import Book,Load

admin.site.register(Book)
admin.site.register(Load)