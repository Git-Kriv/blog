from rest_framework import serializers

from blog.models import Project, Article

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ('id', 'category', 'title', 'client', 'service', 'date', 'duration', 'country', 'context', 'approach')


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ('id', 'title', 'new_agency', 'link')


class ProjectMiniSerializer(serializers.ModelSerializer):

    class Meta:
        model = Project
        fields = ('id', 'category', 'title', 'context')



