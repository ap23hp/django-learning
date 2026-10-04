from django.contrib import admin

from .models import Category, Keyword


class KeywordInline(admin.TabularInline):
    model = Keyword
    extra = 1


class CategoryAdmin(admin.ModelAdmin):
    inlines = [KeywordInline]


admin.site.register(Category, CategoryAdmin)
admin.site.register(Keyword)