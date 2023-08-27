from rest_framework import serializers
from .models import Article

# 將文章序列化為json格式
class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = '__all__'
