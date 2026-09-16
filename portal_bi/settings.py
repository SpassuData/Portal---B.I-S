import os
from dotenv import load_dotenv
from pathlib import Path

load_dotenv(override=True)

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
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
            ],
        },
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

# Azure
AZURE_CLIENT_ID = os.getenv("AZURE_CLIENT_ID")
AZURE_CLIENT_SECRET = os.getenv("AZURE_CLIENT_SECRET")
AZURE_TENANT_ID = os.getenv("AZURE_TENANT_ID")
AZURE_AUTHORITY = f"https://login.microsoftonline.com/{AZURE_TENANT_ID}"
AZURE_SCOPE = ["User.Read"]
REDIRECT_URI = os.getenv("REDIRECT_URI")

# Dashboards - People Analytics
DASHBOARD_PEOPLE_RH           = os.getenv("DASHBOARD_PEOPLE_RH")
DASHBOARD_PEOPLE_CURRICULOS   = os.getenv("DASHBOARD_PEOPLE_CURRICULOS")
DASHBOARD_PEOPLE_TREINAMENTOS = os.getenv("DASHBOARD_PEOPLE_TREINAMENTOS")
DASHBOARD_PEOPLE_PCDS         = os.getenv("DASHBOARD_PEOPLE_PCDS")

# Dashboards - DP Analytics
DASHBOARD_DP_FOLHA   = os.getenv("DASHBOARD_DP_FOLHA")
DASHBOARD_DP_ANALISE = os.getenv("DASHBOARD_DP_ANALISE")

# Dashboards - Performance & Resultados (REMAR)
DASHBOARD_REMAR_GERENTES  = os.getenv("DASHBOARD_REMAR_GERENTES")
DASHBOARD_REMAR_DIRETORIA = os.getenv("DASHBOARD_REMAR_DIRETORIA")

# Dashboards - Ramp Up & Performance
DASHBOARD_RAMPUP_ACOMPANHAMENTO = os.getenv("DASHBOARD_RAMPUP_ACOMPANHAMENTO")

# Dashboards - Workforce Analytics
DASHBOARD_WORKFORCE_VISAO         = os.getenv("DASHBOARD_WORKFORCE_VISAO")
DASHBOARD_WORKFORCE_PRODUTIVIDADE = os.getenv("DASHBOARD_WORKFORCE_PRODUTIVIDADE")
