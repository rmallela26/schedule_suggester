from django.apps import AppConfig
from .Schedule_Finder import Schedule_Finder

scheduler = None

class SchedulesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'schedules'
    def ready(self):
        print("Hello World from apps.py")
        print()
        print()

        global scheduler
        scheduler = Schedule_Finder(['computer science', 'electrical engineering'])
