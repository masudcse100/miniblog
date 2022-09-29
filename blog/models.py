from django.db import models

# Post
class Post(models.Model):
    title = models.CharField(max_length=150)
    desc = models.TextField()

    class Meta:
        ordering = ('-id',)
    