from django.db import models
    # Create your models here.
class Article(models.Model):
    title = models.CharField(max_length = 10) # 標題
    content = models.TextField() # 文章內容
    published_at = models.DateField(auto_now_add=False) # 發布時間
    created_at = models.DateField() # 創建時間
    updated_at = models.DateField() # 更新時間
    
    class Meta:
        db_table = "articles"
