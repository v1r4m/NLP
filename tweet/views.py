#views.py
from django.shortcuts import render
from rest_framework.response import Response
from .models import Post
from rest_framework.views import APIView
from .serializers import DataSerializer
class DataListAPI(APIView):
    def get(self, request):
        queryset = Post.objects.all()
        print(queryset)
        serializer = DataSerializer(queryset, many=True)
        return Response(serializer.data)