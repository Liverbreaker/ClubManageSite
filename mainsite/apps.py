from django.apps import AppConfig


class MainsiteConfig(AppConfig):
    name = 'mainsite'

    def ready(self):
        from miansite import signals
