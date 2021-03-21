from django.apps import AppConfig


class ProSchConfig(AppConfig):
    name = 'pro_sch'
    
    def ready(self):
        import pro_sch.signals
