import uuid
from django.db import models


CATEGORIES_CHOICES = (
    ("Transportation Design", "TD"),
    ("Industrial Design", "ID"),
    ("Retail Space Design", "RSD"),
    ("Packaging Design", "PD"),
    ("Branding and Identity Design", "BID"),
    ("UI UX Design", "UD"),
)


class Project(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    category = models.CharField(max_length=400, choices=CATEGORIES_CHOICES, blank=False)
    title = models.CharField(max_length=400, blank=False)
    client = models.CharField(max_length=4000, blank=True)
    service = models.CharField(max_length=400, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    duration = models.CharField(max_length=400)
    country = models.CharField(max_length=200, default="India", editable=False)
    context = models.TextField(blank=True)
    approach = models.CharField(max_length=400)
    intro_image = models.ImageField(upload_to="projects/", null=False)
    outro_image = models.ImageField(upload_to="projects/", null=True)
    cover_image = models.ImageField(upload_to="projects/", null=True)
    detail_image = models.ImageField(upload_to="projects/", null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Projects"
        ordering = ["-date"]


class Article(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=400)
    news_agency = models.CharField(max_length=400)
    link = models.URLField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Articles"
        ordering = ["-created_at"]


class Client(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    image = models.ImageField(upload_to="projects/", null=False)

    class Meta:
        verbose_name_plural = "Clients"
        ordering = ["id"]
