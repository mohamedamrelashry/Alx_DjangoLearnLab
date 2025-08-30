from django.contrib import admin
from .models import Book

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    # الأعمدة اللي تظهر في صفحة القائمة
    list_display = ('title', 'author', 'publication_year')

    # إضافة فلتر على جانب الصفحة
    list_filter = ('author', 'publication_year')

    # تمكين البحث
    search_fields = ('title', 'author')
from django.contrib import admin
"admin.site.register(CustomUser, CustomUserAdmin)"
# Register your models here.
