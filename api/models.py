# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
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
