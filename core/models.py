from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length = 128)
    content = models.TextField()
    author = models.ForeignKey(User)
    created_at = models.DateTimeField(auto_now_add = True)
    update_at = models.DateTimeField(auto_now = True)

    def __str__(self):
        return '%d - %s' % (self.id, self.title)