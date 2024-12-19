
import os
import django_heroku
from decouple import config
import dj_database_url
import cloudinary
import cloudinary.uploader
import cloudinary.api
import os
import dj_database_url
from dotenv import load_dotenv
import environ

# تهيئة env
env = environ.Env()
environ.Env.read_env()  # تحميل المتغيرات من ملف .env

load_dotenv()




DEBUG = config('DEBUG', default=False, cast=bool)
ALLOWED_HOSTS = ['albaraa-alsadeq.tech', 'www.albaraa-alsadeq.tech']

SECRET_KEY = '123ABczaq$'




# Define BASE_DIR early to avoid errors
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    # whitenoise for static files
    'whitenoise.middleware.WhiteNoiseMiddleware',
]

# After BASE_DIR is defined, use django_heroku settings
django_heroku.settings(locals())


print("Environment Variables:", os.environ)

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.StaticFilesStorage'

print("Current SECRET_KEY:", config('SECRET_KEY'))

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'info',
    'dashboard',

    'cloudinary_storage',
    'cloudinary',

    'ckeditor',
    'rest_framework',
    'portfolio',
]



ROOT_URLCONF = 'portfolio.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
            'libraries':{
                'filter_tags': 'info.templatetags.filter',
            }
        },
    },
]

WSGI_APPLICATION = 'portfolio.wsgi.application'


DATABASES = {
    'default': dj_database_url.config(
        default=os.getenv('DATABASE_URL', 'postgres://USER:PASSWORD@HOST:PORT/DBNAME')
    )
}
# Database settings for development and production

if DEBUG:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': 'django_portfolio',  # قاعدة البيانات المحلية
            'USER': 'postgres',
            'PASSWORD': '123ABczaq$',
            'HOST': 'localhost',
            'PORT': '5432',
        }
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': 'portfoliodatabase1',
            'USER': 'postgres',
            'PASSWORD': '123ABczaq$',
            'HOST': 'portfoliodatabase1.cdkiy46kozvg.eu-north-1.rds.amazonaws.com',
            'PORT': '5432',
        }
    }

    # تكوين Cloudinary لتخزين الملفات في بيئة الإنتاج
    CLOUDINARY_STORAGE = {
        'CLOUD_NAME': 'drys4dgez',
        'API_KEY': '377643715332651',
        'API_SECRET': 'vfoA2eMe6JHXtzM4GYXsSj-wnnI',
    }
    DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'



# Email settings
EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = "alsadeq.albaraagmail.com"
EMAIL_USE_TLS = True
EMAIL_PORT = 587
EMAIL_HOST_USER = config('EMAIL_HOST_USER', default='')
EMAIL_HOST_PASSWORD = config('EMAIL_HOST_PASSWORD', default='')

# Password validation
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

# Internationalization settings
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# Static files (CSS, JavaScript, Images)

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')  # Correct root directory for static files
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'portfolio/static/'),
]

# Media files
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

print(f"Loaded DATABASE_URL: {config('DATABASE_URL', default='NOT FOUND')}")
print(f"Database settings: {DATABASES}")
