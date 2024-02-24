from django.urls import path

from blog.views import project_detail, project_list, article_list, article_detail, project_categories, send_email

urlpatterns = [
    path('projects/', project_list, name='project_list'),
    path('projects/<uuid:pk>/', project_detail, name='project_detail'),
    path('articles/', article_list, name='article_list'),
    path('articles/<uuid:pk>/', article_detail, name='article_detail'),
    path('project-categories/', project_categories, name='article_categories'),
    path('send-email/', send_email, name='send_email')
]