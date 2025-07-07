from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Post(models.Model):

    class PostObjects(models.Manager):
        def get_queryset(self):
            return super().get_queryset().filter(status='published')
    
    options = (
        ('draft', 'Draft'),
        ('published', 'Published')
    )
    
    title = models.CharField(max_length=250)
    excerpt = models.TextField(null=True)
    slug = models.SlugField(max_length=250, unique_for_date='published')
    content = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.PROTECT, default=1)
    published = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='blog_posts'
    )
    status = models.CharField(
        max_length=10,
        choices=options,
        default='published'
    )
    objects = models.Manager()  # Default manager
    post_objects = PostObjects()  # Custom manager for published posts

    class Meta:
        ordering = ('-published',)

    def __str__(self):
        return self.title
    