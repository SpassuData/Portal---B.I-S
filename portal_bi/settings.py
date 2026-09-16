import os
from dotenv import load_dotenv
from pathlib import Path

load_dotenv()

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = os.environ['SECRET_KEY']
DEBUG = os.getenv('DEBUG', 'False').lower() == 'true'
ALLOWED_HOSTS = [h.strip() for h in os.getenv('ALLOWED_HOSTS', '').split(',') if h.strip()]

INSTALLED_APPS = [
    'django.contrib.sessions',
    'django.contrib.staticfiles',
    'core',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
]

# Sem banco de dados por enquanto (portal só exibe links estáticos).
# Sessões assinadas via cookie, sem precisar de tabela django_session.
SESSION_ENGINE = 'django.contrib.sessions.backends.signed_cookies'

ROOT_URLCONF = 'portal_bi.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
    },
]

STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / 'static']
STATIC_ROOT = BASE_DIR / 'staticfiles'

STORAGES = {
    'staticfiles': {
        'BACKEND': 'whitenoise.storage.CompressedManifestStaticFilesStorage',
    },
}

# Azure AD / Microsoft Entra ID (login via Microsoft)
# Usamos os.environ[...] (em vez de os.getenv) de propósito: se uma dessas faltar,
# o app quebra já na inicialização com um erro claro, em vez de silenciosamente
# virar None e gerar um erro confuso da Microsoft (ex.: AADSTS90102) mais tarde.
AZURE_CLIENT_ID = os.environ['AZURE_CLIENT_ID']
AZURE_CLIENT_SECRET = os.environ['AZURE_CLIENT_SECRET']
AZURE_TENANT_ID = os.environ['AZURE_TENANT_ID']
REDIRECT_URI = os.environ['REDIRECT_URI']

AZURE_AUTHORITY = f"https://login.microsoftonline.com/{AZURE_TENANT_ID}"
AZURE_SCOPE = ["User.Read"]

# Dashboards
DASHBOARD_RH = os.getenv("DASHBOARD_RH")
DASHBOARD_FIN = os.getenv("DASHBOARD_FIN")
DASHBOARD_OP = os.getenv("DASHBOARD_OP")