from rest_framework import serializers
from .models import Article

# 將 models.py 定義的 Article 中所有欄位轉換成可以傳輸的模式
class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article 
        fields = '__all__' # 輸出所有欄位
