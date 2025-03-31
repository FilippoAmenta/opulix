import os
import environ
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

print(BASE_DIR)
env = environ.Env()
environ.Env.read_env(os.path.join(BASE_DIR, ".env"))

DEBUG = env.bool("DEBUG", default=False)

SECRET_KEY = env.str('SECRET_KEY', default='django-insecure-!@#qwertyuiop')

ALLOWED_HOSTS = env.list("ALLOWED_HOSTS")

INSTALLED_APPS = [
    'mptt',
    'unfold',  
    'unfold.contrib.forms',
    'unfold.contrib.import_export',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.humanize',
    'import_export',
    'colorfield',
    'treenode',
    'djmoney',
    'apps.expenses'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'core.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            BASE_DIR / "templates",
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'core.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': env.str('DB_ENGINE', default='django.db.backends.sqlite3'),
        'NAME': env.str('DB_NAME', default=os.path.join(BASE_DIR, 'db.sqlite3')),
    }
}

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

STATIC_URL = 'static/'

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')


DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

CURRENCY_CHOICES = [('EUR', '€')]

from django.urls import reverse_lazy

UNFOLD = {
    "SITE_TITLE": "Opulix",
    "SITE_HEADER": "Opulix",
    "SITE_SUBHEADER": "Your finance, simplified.",
    "BORDER_RADIUS": "0px",
    "COLORS": {
        "base": {
            "50": "250 250 249",
            "100": "245 245 244",
            "200": "231 229 228",
            "300": "214 211 209",
            "400": "168 162 158",
            "500": "120 113 108",
            "600": "87 83 78",
            "700": "68 64 60",
            "800": "41 37 36",
            "900": "28 25 23",
            "950": "12 10 9"
        },
        "primary": {
            "50": "255 241 242",
            "100": "255 228 230",
            "200": "254 205 211",
            "300": "253 164 175",
            "400": "251 113 133",
            "500": "244 63 94",
            "600": "225 29 72",
            "700": "190 18 60",
            "800": "159 18 57",
            "900": "136 19 55",
            "950": "76 5 25"
        }
    },
    "SIDEBAR": {
        "show_search": True, 
        "show_all_applications": False,
        "navigation": [
            {
                "title": "Expenses",
                "separator": True,
                "collapsible": True,
                "items": [
                    {
                        "title": "Expenses",
                        "icon": "payments",
                        "link": reverse_lazy("admin:expenses_expense_changelist"),
                    },
                    {
                        "title": "Expenses categories",
                        "icon": "category",
                        "link": reverse_lazy("admin:expenses_expensecategory_changelist"),
                    },
                     {
                        "title": "Expenses tags",
                        "icon": "sell",
                        "link": reverse_lazy("admin:expenses_expensetag_changelist"),
                    },
                ],
            },
        ],
    },
}