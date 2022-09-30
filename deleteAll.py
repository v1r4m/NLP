import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "nlpdjango.settings") #get venv
import django
django.setup()
from tweet.models import Post, LatestLink
Post.objects.all().delete()
LatestLink.objects.all().delete()