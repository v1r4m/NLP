from asyncio.windows_events import NULL
from django.conf import settings
from django.db import models
from django.utils import timezone

class Post(models.Model):
    pkWord = models.CharField(max_length=10)
    join_word = models.CharField(max_length=10)
    join_v = models.IntegerField()
    #pk = models.ForeignKey('tweet.Link') #####
    #pkWord = models.CharField(max_length=10)

    def __str__(self):
        return self.pkWord

class LatestLink(models.Model):
    link = models.CharField(max_length=19)
    word = models.CharField(max_length=10, default=NULL)
    def __str__(self):
        return self.word