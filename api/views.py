from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from .models import Articles
from .serializers import ArticleSerializer
from rest_framework.decorators import api_view

# Create your views here. (創建api)
@api_view(['GET'])
def api_overview(request):
    api_urls={
        'article list':'/article_list',
        'article create':'/article_create',
        'article delete':'/article_delete'
    }
    return Response(api_urls)

@api_view(['GET'])
def article_list(request):
    pass