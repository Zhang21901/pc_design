import os

SECRET_KEY = os.environ.get("SUPERSET_SECRET_KEY", "0nP0p5zUn25DimserkOM/3J+M6+N5AZgUVOBuGduE/Myy2tFi2dDMkVl")

DB_HOST = os.environ.get("DB_HOST", "localhost")
DB_PORT = os.environ.get("DB_PORT", "3306")
DB_NAME = os.environ.get("DB_NAME", "superset_db")
DB_USER = os.environ.get("DB_USER", "superset_user")
DB_PASSWORD = os.environ.get("DB_PASSWORD", "123456")

SQLALCHEMY_DATABASE_URI = f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
BABEL_DEFAULT_LOCALE = 'zh'
LANGUAGES = {
    'zh': {'flag': 'cn', 'name': '简体中文'},
    'en': {'flag': 'us', 'name': 'English'},
}
SUPERSET_WEBSERVER_PROXY_FIX = 1
WTF_CSRF_ENABLED =False #禁用了 CSRF 保护
CONTENT_SECURITY_POLICY = {
    'script-src': "'self' 'unsafe-inline'",  # 允许内联脚本
    'object-src': "'none'",
    'base-uri': "'self'",
    'frame-ancestors': "'self'"
}
