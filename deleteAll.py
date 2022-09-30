import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "nlpdjango.settings") #get venv
import django
django.setup()
from tweet.models import Post
Post.objects.all().delete()