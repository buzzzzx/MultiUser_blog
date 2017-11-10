from django.db import models

from account.models import UserProfile
from blog.models import Post


# Create your models here.

class PostComment(models.Model):
    post = models.ForeignKey(Post, related_name='comments')  # 可通过post.comments.all()
    user = models.ForeignKey(UserProfile, related_name='blog_comments')  # 可通过user.blog_comments.all()取回所有评论
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return 'Comment by {} on {}'.format(self.user.username, self.post)
