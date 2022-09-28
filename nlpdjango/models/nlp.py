from __future__ import unicode_literals

from django.db import models
from django.utils import timezone

class Tquery(models.Model):
    
    pk = models.ForeignKey('tweet.Word')
    pkLink = models.TextField()
    #pk = models.ForeignKey('tweet.Link') #####
    #pkWord = models.CharField(max_length=10)
    join_words = models.ManyToManyField('tweet.Word',
                        verbose_name=u'relate', blank=True,
                        related_name='join_word')

from django.contrib import admin
from nlpdjango.models.nlp import Tquery

admin.site.register(Tquery)