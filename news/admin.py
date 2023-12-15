from django.contrib import admin
from .models import News

class ArticleAdmin(admin.ModelAdmin):
    list_display = ("sarlavha", "taglavha",)
    prepopulated_fields = {"slug": ("sarlavha",)} 

# Register your models here.
admin.site.register(News, ArticleAdmin)