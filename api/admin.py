from django.contrib import admin
from .models import User, Book, Chapter, Category

# Register your models here.
admin.site.register(User)
admin.site.register(Category)

@admin.register(Chapter)
class ChapterAdmin(admin.ModelAdmin):
    list_display = ['title', 'book']
    autocomplete_fields = ['book']  # Thêm vào đây để kích hoạt tìm kiếm AJAX

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    search_fields = ['title']
