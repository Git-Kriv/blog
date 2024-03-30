from django.contrib import admin

# Register your models here.
from blog.models import Project, Article, Client


class ProjectAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "category",
        "client",
        "service",
        "date",
        "duration",
        "country",
        "approach",
    )
    list_filter = ("category",)
    search_fields = (
        "title",
        "category",
        "client",
        "service",
        "date",
        "duration",
        "country",
        "approach",
    )
    ordering = ["date"]


class ArticleAdmin(admin.ModelAdmin):
    list_display = ("title", "news_agency", "link")
    list_filter = ("news_agency",)
    search_fields = ("title", "news_agency", "link")
    ordering = ["title"]


admin.site.register(Project, ProjectAdmin)
admin.site.register(Article, ArticleAdmin)
admin.site.register(Client)

