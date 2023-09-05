FROM python:3.7-alpine

# 創建工作目錄 app
WORKDIR /app

COPY requirements.txt .

RUN pip3 install -r requirements.txt --no-cache-dir

# 將所有檔案移到工作目錄 app 底下
COPY . /app

# 暴露 8000 port
EXPOSE 8000 

# 後端啟動服務
CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]
