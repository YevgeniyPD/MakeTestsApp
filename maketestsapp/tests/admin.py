from django.contrib import admin

from .models import Tests

@admin.register(Tests)
class ArticleAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)} 