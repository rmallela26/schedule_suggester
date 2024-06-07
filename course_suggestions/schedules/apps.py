from django.apps import AppConfig

scheduler = None

class SchedulesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'schedules'
    def ready(self):
        from .Schedule_Finder import Schedule_Finder
        print("Hello World from apps.py")
        print()
        print()

        global scheduler
        if scheduler is None:
            scheduler = Schedule_Finder(['computer science', 'electrical engineering'])
