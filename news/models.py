from django.db import models
from uuid import uuid4

# Create your models here.

class News(models.Model):
    # id = models.PositiveIntegerField(unique=True, primary_key=True)
    date_created = models.DateField(auto_now=True)
    date_published = models.DateField()
    author = models.CharField(max_length=255)
    source = models.CharField(max_length=255)
    title = models.CharField(max_length=255, unique=True)
    url = models.CharField(max_length=255)
    tags = models.CharField(max_length= 100)
    # category = models.ForeignKey(Category, on_delete=models.CASCADE)
    slug = models.SlugField(unique=True, default=uuid4)
    excerpt = models.TextField()
    content = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title