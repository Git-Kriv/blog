from rest_framework import serializers
from django.conf import settings
from blog.models import Project, Article

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ('id', 'category', 'title', 'client', 'service', 'date', 'duration', 'country', 'context', 'approach', 'long_image1', 'long_image2', 'short_image1', 'short_image2')


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ('id', 'title', 'news_agency', 'link')


class ProjectMiniSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ('id', 'category', 'title', 'context', 'short_image1')

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['short_image1'] = instance.short_image1.url
        return data



