from django.apps import AppConfig


class ThuvienbkConfig(AppConfig):
    name = 'thuvienbk'

    def ready(self):
        import thuvienbk.signals