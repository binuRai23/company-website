from django.apps import AppConfig
import signal

class LunarappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'lunarApp'
    def ready(self):
        import lunarApp.signals



    