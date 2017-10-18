SECRET_KEY = 'fake-key'

INSTALLED_APPS = (
    'django_tabulate',
    'tests',
)

TABULATE_DEFAULTS = {
    'tablefmt': 'simple'
}

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': ':memory:'
    }
}