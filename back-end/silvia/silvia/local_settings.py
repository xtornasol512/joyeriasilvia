# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'r74uc+u0l$7$(ng8a$4u1$(t@l)r(^s_d)l!-*og8j$7-w6-fj'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'db.sqlite3',
    }
}