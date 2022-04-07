from django.apps import AppConfig


class FazlaGidaConfig(AppConfig):
    name = "FazlaGidaChallenge"

    def ready(self):
        from FazlaGidaChallenge.signals import user  # noqa
