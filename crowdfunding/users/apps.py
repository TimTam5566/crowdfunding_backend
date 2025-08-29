from django.apps import AppConfig
''' This chelps Django: Register the app properly

Apply migrations Load signals, models, and other app-specific logic'''

class UsersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'users'
