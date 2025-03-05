#!/bin/bash

source .env

echo "正在创建 Conda 环境..."
conda env create -f environment.yml

echo "激活 Conda 环境..."
conda activate analysis

echo "安装 Python 依赖..."
pip install -r requirements.txt

echo "启动 MySQL 并导入数据库..."
mysql -u root -p"$DB_PASSWORD" -e "
    CREATE DATABASE IF NOT EXISTS ${DB_NAME} CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
    CREATE USER IF NOT EXISTS '${DB_USER}'@'localhost' IDENTIFIED BY '${DB_PASSWORD}';
    GRANT ALL PRIVILEGES ON ${DB_NAME}.* TO '${DB_USER}'@'localhost';
    FLUSH PRIVILEGES;
"
mysql -u "$DB_USER" -p"$DB_PASSWORD" "$DB_NAME" < superset_dump.sql

echo "初始化 Superset 数据库..."
superset db upgrade

echo "初始化 Superset..."
superset init

echo "编译前端代码..."
cd superset-frontend
npm install
npm run build
cd ..

echo "启动 Superset..."
superset run -p 8080