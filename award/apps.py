from django.apps import AppConfig


class AwardConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'award'



class UserConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'users'


    def ready(self):
        
        import users.signals