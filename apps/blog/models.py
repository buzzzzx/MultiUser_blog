from django.db import models
from django.utils import timezone
from datetime import datetime
from django.core.urlresolvers import reverse
from taggit.managers import TaggableManager

from account.models import UserProfile
from utils.randstr import generate_code


# Create your models here.

class PublishedManager(models.Manager):
    def get_queryset(self):
        return super(PublishedManager, self).get_queryset().filter(status='published')


class Post(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )
    title = models.CharField(max_length=50)
    uu_id = models.CharField(max_length=8, default=generate_code)
    author = models.ForeignKey(UserProfile, related_name='blog_posts')
    body = models.TextField()
    publish = models.DateTimeField(default=datetime.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='published')
    published = PublishedManager()
    objects = models.Manager()  # the default
    # tags
    tags = TaggableManager()

    class Meta:
        ordering = ('-publish',)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:post_detail',
                       args=[self.publish.year, self.publish.strftime('%m'), self.publish.strftime('%d'), self.uu_id])
