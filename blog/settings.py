"""
Django settings for blog project.

Generated by 'django-admin startproject' using Django 2.2.6.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '47!-e)rc)#g*@5w#d%4hm+58ge*2hva82-t+-dq!s(u#+u!xxb'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'posts',
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

ROOT_URLCONF = 'blog.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR,"template")],
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

WSGI_APPLICATION = 'blog.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    },
    # 'default': {
    #     'ENGINE': 'django.db.backends.mysql',
    #     'NAME': 'blog_test',
    #     'USER':'luohua',
    #     'PASSWORD':'1qaz@WSX',
    #     'HOST':'118.25.181.239',
    #     'PORT':'3306',
    #     }
}


# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/2.2/topics/i18n/

#LANGUAGE_CODE = 'en-us'

#TIME_ZONE = 'UTC'
# 把英文改为中文
LANGUAGE_CODE = 'zh-hans'

# 把国际时区改为中国时区（东八区）
TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = '/static/'


# STATIC_ROOT 是在部署的时候才发挥作用, 而实际情况下,静态文件的一般安放位置有两种:
# 1.一种就是在每个app里面新建一个static文件夹,将静态文件放到里面,在加载静态文件时,比如要在模板中用到静态文件,
# django会自动在每个app里面搜索static文件夹(所以,不要把文件夹的名字写错哦, 否则django就找不到你的文件夹了)
# 2.另一种,就是在所有的app文件外面,建立一个公共的文件夹, 因为有些静态文件不是某个app独有的,那么就可以把它放到一个公共文件夹里面,
# 方便管理(注意,建立一个公共的静态文件的文件夹只是一种易于管理的做法,但是不是必须的,app是可以跨app应用静态文件的,
# 因为最后所有的静态文件都会在STATIC_ROOT里面存在)
# 那现在的问题是如何让django知道你把一些静态文件放到app以外的公共文件夹中呢,那就需要配置STATICFILES_DIRS了


STATICFILES_DIRS  = (
    os.path.join(BASE_DIR,"static"),
                )


#MEDIA_ROOT
#AUTH_USER_MODEL