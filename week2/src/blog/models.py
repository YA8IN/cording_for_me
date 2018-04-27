from django.db import models

# Create your models here.
class Article(models.Model):
    tilte = models.CharField(max_length=30)
    contents = models.TextField()
    view_count = models.IntField()

class Comment(models.Model):
    article = models.ForeignKey(Article)
    comment = models.CharField(max_length=100)
