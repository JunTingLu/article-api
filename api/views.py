from api.models import Article
from api.serializers import ArticleSerializer
from rest_framework.decorators import api_view
from rest_framework import viewsets

# Create your views here. (創建api)
class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

