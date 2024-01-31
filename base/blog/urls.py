from django.urls import path

from blog.views import project_detail, project_list, article_list, article_detail

urlpatterns = [
    path('projects/', project_list, name='project_list'),
    path('projects/<uuid:pk>/', project_detail, name='project_detail'),
    path('articles/', article_list, name='article_list'),
    path('articles/<uuid:pk>/', article_detail, name='article_detail'),
]