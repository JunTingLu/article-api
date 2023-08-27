from rest_framework import serializers
from .models import Articles

# 將文章序列化為json格式
class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Articles
        fields = '__all__'
