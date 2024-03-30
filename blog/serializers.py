from rest_framework import serializers
from django.conf import settings
from blog.models import Project, Article, Client


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = (
            "id",
            "category",
            "title",
            "client",
            "service",
            "date",
            "duration",
            "country",
            "context",
            "approach",
            "intro_image",
            "outro_image",
            "cover_image",
            "detail_image",
        )


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ("id", "title", "news_agency", "link")


class ProjectMiniSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ("id", "category", "title", "context", "cover_image")

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data["cover_image"] = instance.cover_image.url
        return data


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = "__all__"
