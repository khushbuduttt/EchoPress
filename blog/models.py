from django.db import models
from django_ckeditor_5.fields import CKEditor5Field

from blog.storage import BlogImageStorage
from core.models import GenericModel
from django.utils.text import slugify
import re



#--------------------- category ----------------------------#
class Category(GenericModel):
    name = models.CharField(
        max_length=100,
        unique=True)
    slug = models.SlugField(
        max_length=100,
        unique=True,
        blank=True)
    description = models.TextField(
        blank=True
    )

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

#--------------------- tag ----------------------------#
class Tag(GenericModel):
    name = models.CharField(
        max_length=50,
        unique=True,
        null = True,
        blank = True
    )
    slug = models.SlugField(
        max_length=50,
        unique=True,
        blank=True
    )
    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)
#--------------------- post ----------------------------#
class Post(GenericModel):
    title = models.CharField(
        max_length=200
    )
    subtitle = models.CharField(
        max_length=200,
        null=True,
        blank=True
    )
    slug = models.SlugField(
        unique=True,
        null=True,
        blank=True
    )
    content = CKEditor5Field(
        config_name='extends'
    )
    excerpt = models.TextField(
        null=True,
        blank=True
    )
    body = models.TextField()
    tag = models.ManyToManyField(
        Tag,
        related_name='articles',
        blank=True
    )
    category = models.ManyToManyField(
        Category,
        blank=True
    )
    image = models.ImageField(
        upload_to='post/',
    storage = BlogImageStorage(),
        blank=True,
        null=True
    )

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)
