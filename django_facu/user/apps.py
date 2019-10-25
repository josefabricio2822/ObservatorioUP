from django.apps import AppConfig


class UsersConfig(AppConfig):
    name = 'user'
    #No entiendo la funcion ready()
    def ready(self):
        import user.signals