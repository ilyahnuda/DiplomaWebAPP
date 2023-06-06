from django.db import models

from ..Models.Author import Author


class News(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    authors = models.ManyToManyField(Author)
    time = models.DateTimeField()
    img = models.CharField(max_length=200, null=True)
    text = models.TextField()
    img_description = models.CharField(max_length=500, null=True)
    link = models.CharField(max_length=200, null=True)
