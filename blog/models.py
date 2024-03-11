import uuid
from django.db import models

# Create your models here.


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
    category = models.CharField(max_length=50, choices=CATEGORIES_CHOICES, blank=False)
    title = models.CharField(max_length=200, blank=False)
    client = models.CharField(max_length=50, blank=True)
    service = models.CharField(max_length=50, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    duration = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    context = models.TextField(blank=True)
    approach = models.CharField(max_length=50)
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
    title = models.CharField(max_length=50)
    news_agency = models.CharField(max_length=50)
    link = models.URLField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Articles"
        ordering = ["-created_at"]

