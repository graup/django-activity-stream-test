from django.apps import AppConfig
from django.contrib.auth import get_user_model


class ExampleConfig(AppConfig):
    name = 'example'

    def ready(self):
        from actstream import registry
        registry.register(self.get_model('Notification'))
        registry.register(get_user_model())
