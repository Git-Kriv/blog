import uuid
from django.db import models
from PIL import Image, ExifTags, ImageOps
from io import BytesIO
from django.core.files.uploadedfile import InMemoryUploadedFile

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

    def compress_image(self, image):
        img = Image.open(image)
        img_io = BytesIO()
        img = img.convert("RGB")
        img = ImageOps.exif_transpose(img)

        img.save(img_io, format="JPEG", quality=70)
        img_io.seek(0)
        return InMemoryUploadedFile(
            img_io,
            "ImageField",
            image.name,
            "image/jpeg",
            img_io.getbuffer().nbytes,
            None,
        )

    class Meta:
        verbose_name_plural = "Projects"
        ordering = ["-date"]

    def save(self, *args, **kwargs):
        if self.intro_image:
            self.intro_image = self.compress_image(self.intro_image)
        if self.outro_image:
            self.outro_image = self.compress_image(self.outro_image)
        if self.cover_image:
            self.cover_image = self.compress_image(self.cover_image)
        if self.detail_image:
            self.detail_image = self.compress_image(self.detail_image)
        super(Project, self).save(*args, **kwargs)


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

    def compress_image(self, image):
        img = Image.open(image)
        img_io = BytesIO()
        img = img.convert("RGB")
        img = ImageOps.exif_transpose(img)
        img.save(img_io, format="JPEG", quality=70)
        img_io.seek(0)
        return InMemoryUploadedFile(
            img_io,
            "ImageField",
            image.name,
            "image/jpeg",
            img_io.getbuffer().nbytes,
            None,
        )

    def save(self, *args, **kwargs):
        if self.image:
            self.image = self.compress_image(self.image)
        super(Client, self).save(*args, **kwargs)
