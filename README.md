# Article API Demo

主要透過 Django 設計具有 CRUD 功能的 API，讓使用者以 JWT 模擬針對文章資料庫做操作。

## 簡介

- 後端採用 Python Django 框架及 Django REST Framework
- 使用者登入採用 Django REST Frqmwork SimpleJWT
- 支援新增、刪除、修改 Django API

## 線上測試

- 訪問地址：TODO

## JWT 

- 有效期限：30 days

## 環境

- Django 3.2
- Python 3.7
- Docker Compose v2.20.2
- PostgreSQL

## Docker-Compose 啟動服務

- 安裝 Docker (Windows)

可參考 https://docs.docker.com/desktop/install/windows-install/

- 執行專案

Run services.
```
docker compose up -d --build
```
Close services.
```
docker compose down   
```
Restart services.
```
docker-compose restart
```

