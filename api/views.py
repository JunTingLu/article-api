from api.models import Article
from api.serializers import ArticleSerializer
from rest_framework.response import Response
from rest_framework import viewsets, status
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from drf_yasg.utils import swagger_auto_schema

# Create your views here.
class ArticleViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated] # 為這個視圖加上 IsAuthenticated 認證
    queryset = Article.objects.all() # 基礎的查詢條件
    serializer_class = ArticleSerializer # 序列化器

    # 取得文章列表 
    def list(self, request):
        # 避免快取，需要再次查詢
        queryset = Article.objects.all()
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # 取得單一文章
    def retrieve(self, request, pk=None): # 指定 primary key
        # 取得文章，否則回應 404
        article = get_object_or_404(self.queryset, pk=pk) 
        serializer = self.serializer_class(article)
        return Response(serializer.data)
    
    # 新增文章
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        # 若資料驗證通過，就儲存
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    # 修改文章
    def update(self, request, pk=None, *args, **kwargs):
        # 取得文章，否則回應 404
        article = get_object_or_404(self.queryset, pk=pk)
        serializer = self.serializer_class(article, data=request.data)
        # 若資料驗證通過，就修改
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    # 刪除文章
    def destroy(self, request, pk=None):
        # 取得文章，否則回應 404
        article = get_object_or_404(self.queryset, pk=pk)
        # 刪除文章
        article.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)
