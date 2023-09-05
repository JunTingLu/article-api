from django.apps import AppConfig

class ApiConfig(AppConfig):
    # 設定預設的自動增加主鍵(primary key)欄位為 BigAutoField
    default_auto_field = 'django.db.models.BigAutoField'
    # app 名稱
    name = 'api'
