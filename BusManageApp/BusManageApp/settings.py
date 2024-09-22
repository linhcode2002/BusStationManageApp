"""
Django settings for BusManageApp project.

Generated by 'django-admin startproject' using Django 5.0.3.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.0/ref/settings/
"""

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-lu_&txn+tjs@ha_h$32+1+d45g=q8-b&gd)mt)c)cf9*mr3nhx'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

from django.utils import timezone

TIME_ZONE = 'Asia/Ho_Chi_Minh'
USE_TZ = True

# Application definition

INSTALLED_APPS = [
    'jazzmin',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'BusManage.apps.BusManageConfig',
    'ckeditor',
    'ckeditor_uploader',
    'rest_framework',
    'oauth2_provider',
    'drf_yasg',
    'debug_toolbar',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'BusManage.middleware.CacheControlMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    "debug_toolbar.middleware.DebugToolbarMiddleware"
]

INTERNAL_IPS = [
    "127.0.0.1",
]

ROOT_URLCONF = 'BusManageApp.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

JAZZMIN_SETTINGS = {
    "site_title": "Bus Management Admin",
    "site_header": "Bus Management",
    "site_brand": "Bus Management",
    "site_logo": "bus/img/logo.png",  # Đường dẫn tới logo của bạn
    "login_logo": None,
    "login_logo_dark": None,
    "site_logo_classes": "img-circle",
    "site_icon": None,
    "welcome_sign": "Welcome to Bus Management Admin",
    "copyright": "Bus Management Ltd",

    # Các model bạn muốn tìm kiếm
    "search_model": [
        "auth.User",
        # "bus.Customer",
        # "bus.BusRoute",
        # "bus.Trip",
        # "bus.Booking",
        # "bus.Review",
        # "bus.RevenueStatistics",
    ],

    "user_avatar": "avatar",  # Sử dụng trường avatar từ model User

    "topmenu_links": [
        {"name": "Home", "url": "admin:index", "permissions": ["auth.view_user"]},
        {"name": "Support", "url": "https://github.com/farridav/django-jazzmin/issues", "new_window": True},
        {"model": "auth.User"},
        {"app": "bus"},
    ],

    "usermenu_links": [
        {"name": "Support", "url": "https://github.com/farridav/django-jazzmin/issues", "new_window": True},
        {"model": "auth.user"}
    ],

    "show_sidebar": True,
    "navigation_expanded": True,

    # Không ẩn ứng dụng hay model nào
    "hide_apps": [],
    "hide_models": [],

    # Thứ tự hiển thị các ứng dụng và model
    "order_with_respect_to": ["auth", "bus", "Customer", "BusRoute", "Trip",
                              "Booking", "Review", "RevenueStatistics"],

    "custom_links": {
        "bus": [{
            "name": "Manage Reviews",
            "url": "manage_reviews",
            "icon": "fas fa-star",
            "permissions": ["bus.view_review"]
        }]
    },

    # Đặt icon cho các model
    "icons": {
        "auth": "fas fa-users-cog",
        "auth.user": "fas fa-user",
        "auth.Group": "fas fa-users",
        "bus.Customer": "fas fa-user",
        "bus.BusRoute": "fas fa-route",
        "bus.Trip": "fas fa-bus",
        "bus.Booking": "fas fa-ticket-alt",
        "bus.Review": "fas fa-star",
        "bus.RevenueStatistics": "fas fa-chart-line",
    },
    "default_icon_parents": "fas fa-chevron-circle-right",
    "default_icon_children": "fas fa-circle",

    "related_modal_active": False,

    "custom_css": None,
    "custom_js": None,
    "use_google_fonts_cdn": True,
    "show_ui_builder": False,

    "changeform_format": "horizontal_tabs",
    "changeform_format_overrides": {"auth.user": "collapsible", "auth.group": "vertical_tabs"},
    "language_chooser": False,
}


WSGI_APPLICATION = 'BusManageApp.wsgi.application'



# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'bus_manage',
        'USER': 'root',
        'PASSWORD': 'Admin@123',
        'PORT': '3307',
        'HOST': ''
    }
}

CLIENT_ID = 'n4yjvSnqOIdMDBVDRbE7WJCqxdWmG56ba2g3plQR'
CLIENT_SECRET = '3lRV8xvZMiCQYgOiP9umz4Qi8chD2eByi0BppGR43LWttjKKwpSv8Ql7ada4p9w0uFuOPdwkmukQeHfdE8sFOMmZQteHvOYJbCUh4gmOxaqLyzOWZ8vaEnaOzOPsEl5R'

REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 5,
    'DEFAULT_AUTHENTICATION_CLASSES': ('oauth2_provider.contrib.rest_framework.OAuth2Authentication',
                                       )}

import cloudinary

cloudinary.config(
    cloud_name="dx9aknvnz",
    api_key="853573281637597",
    api_secret="tlIQH3E4bQ3TM1XhLh2GqGpJNeA"
)

# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

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

AUTH_USER_MODEL = 'BusManage.User'
# Internationalization
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_ROOT = '/home/linhhv/BusStationManageApp/static/'
STATIC_URL = 'static/'
MEDIA_ROOT = '%s/BusManage/static/' % BASE_DIR
CKEDITOR_UPLOAD_PATH = "ckeditor/images/"
CLOUDINARY_URL = "cloudinary://853573281637597:tlIQH3E4bQ3TM1XhLh2GqGpJNeA@dx9aknvnz"

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
