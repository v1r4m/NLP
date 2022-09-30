from django.conf import settings
from django.db import models
from django.utils import timezone

class Post(models.Model):
    pkWord = models.CharField(max_length=10)
    join_word = models.CharField(max_length=10)
    join_v = models.IntegerField()
    published_date = models.DateTimeField(blank=True, null=True)
    #pk = models.ForeignKey('tweet.Link') #####
    #pkWord = models.CharField(max_length=10)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.pkWord

class LatestLink(models.Model):
    link = models.CharField(max_length=19)

    def __str__(self):
        return self.link