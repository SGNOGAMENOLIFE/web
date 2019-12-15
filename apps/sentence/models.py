from django.db import models
from books.models import Book
# Create your models here.


class Sentence(models.Model):

    book = models.ForeignKey(Book, on_delete=False)
    poster = models.CharField(default="", null=True, blank=True)
    post_time = models.DateTimeField(default=0)
    source = models.CharField(default="")
    author = models.CharField()
    text = models.TextField()
    click_num = models.IntegerField()
    collection_num = models.IntegerField()




