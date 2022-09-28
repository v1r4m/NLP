from django.conf import settings
from django.db import models
from django.utils import timezone


class Post(models.Model):
    pkWord = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    pkLink = models.TextField()
    #pk = models.ForeignKey('tweet.Link') #####
    #pkWord = models.CharField(max_length=10)
    join_words = models.ManyToManyField(settings.AUTH_USER_MODEL,
                        verbose_name=u'relate', blank=True,
                        related_name='join_word')

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.pkLink