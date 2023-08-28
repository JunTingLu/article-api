from api.models import Article
from api.serializers import ArticleSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import viewsets, status
from django.shortcuts import get_object_or_404

# Create your views here. (創建api)
class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

    def list(self, request):
        queryset = Article.objects.all()
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def retrieve(self, request, pk=None):
        article = get_object_or_404(self.queryset, pk=pk)
        serializer = self.serializer_class(article)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def update(self, request, pk=None, *args, **kwargs):
        article = get_object_or_404(self.queryset, pk=pk)
        serializer = self.serializer_class(article, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def destroy(self, request, pk=None):
        article = get_object_or_404(self.queryset, pk=pk)
        article.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)
