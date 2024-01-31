from django.contrib import admin

# Register your models here.
from blog.models import Project, Article


class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'client', 'service', 'date', 'duration', 'country', 'approach')
    list_filter = ('category', 'client', 'service', 'date', 'duration', 'country', 'approach')
    search_fields = ('title', 'category', 'client', 'service', 'date', 'duration', 'country', 'approach')
    ordering = ['date']

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'new_agency', 'link')
    list_filter = ('title', 'new_agency', 'link')
    search_fields = ('title', 'new_agency', 'link')
    ordering = ['title']


admin.site.register(Project)
admin.site.register(Article)