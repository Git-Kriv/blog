from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.pagination import PageNumberPagination

from django.core.mail import send_mail

from blog.models import Project, Article, Client
from blog.serializers import (
    ProjectSerializer,
    ArticleSerializer,
    ProjectMiniSerializer,
    ClientSerializer,
)


PAGE_SIZE = 10


@api_view(["GET", "POST"])
# NOTE: ADD Permission classes here if authentication is needed for the API
# @permission_classes((IsAuthenticated,)), etc...
def project_list(request, format=None):
    """
    List all projects, or create a new project.
    """
    if request.method == "GET":
        paginator = PageNumberPagination()
        paginator.page_size = PAGE_SIZE
        projects = Project.objects.all()
        result_page = paginator.paginate_queryset(projects, request)
        serializer = ProjectMiniSerializer(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)

    elif request.method == "POST":
        data = request.data
        serializer = ProjectMiniSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET", "PUT", "DELETE"])
# NOTE: ADD Permission classes here if authentication is needed for the API
# @permission_classes((IsAuthenticated,)), etc...
def project_detail(request, pk, format=None):
    """
    Retrieve, update or delete a project instance.
    """
    try:
        project = Project.objects.get(pk=pk)
    except Project.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer = ProjectSerializer(project)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    elif request.method == "PUT":
        data = request.data  # since DATA is deprecated
        serializer = ProjectSerializer(project, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == "DELETE":
        project.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(["GET", "POST"])
# NOTE: ADD Permission classes here if authentication is needed for the API
# @permission_classes((IsAuthenticated,)), etc...
def article_list(request, format=None):
    """
    List all articles, or create a new article.
    """
    if request.method == "GET":
        articles = Article.objects.all()
        serializer = ArticleSerializer(articles, many=True)
        return Response(serializer.data)

    elif request.method == "POST":
        data = request.data
        serializer = ArticleSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET", "PUT", "DELETE"])
# NOTE: ADD Permission classes here if authentication is needed for the API
# @permission_classes((IsAuthenticated,)), etc...
def article_detail(request, pk, format=None):
    """
    Retrieve, update or delete an article instance.
    """
    try:
        article = Article.objects.get(pk=pk)
    except Article.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer = ArticleSerializer(article)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    elif request.method == "PUT":
        data = request.data  # since DATA is deprecated
        serializer = ArticleSerializer(article, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == "DELETE":
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(["GET"])
def project_categories(request, format=None):
    """
    List all articles by category.
    """
    try:
        category = request.GET.get("category")
        print(category)

    except Exception as e:
        print(request.data)
        return Response(
            data={"ERROR": "NO CATEGORY"}, status=status.HTTP_400_BAD_REQUEST
        )
    projects = Project.objects.filter(category=category)
    if projects is not None:
        serializer = ProjectMiniSerializer(projects, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(data={"ERROR": "NO CONTENT"}, status=status.HTTP_404_NOT_FOUND)


@api_view(["POST", "GET"])
def send_email(request, format=None):
    """
    Send an email.
    """
    try:
        data = request.data
        message = f" Name: {data['name']}\n Email: {data['email']}\n Company: {data['company']}\n Requirements: {data['requirements']}"
        print(data)
        send_mail(
            "Mail From Utpanna Website",
            message,
            "kriv.connect@gmai.com",
            ["kriv.temp@gmail.com"],
            fail_silently=False,
        )
        return Response(status=status.HTTP_200_OK)
    except Exception as e:
        print(e)
        return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET"])
def get_client(request, format=None):
    """
    Get client details.
    """
    try:
        client = Client.objects.all()
        serializer = ClientSerializer(client, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except Exception as e:
        print(e)
        return Response(status=status.HTTP_400_BAD_REQUEST)
