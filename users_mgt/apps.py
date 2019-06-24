from django.apps import AppConfig


class UsersConfig(AppConfig):
    name = 'users_mgt'
    verbose_name = 'users'

    def ready(self):
        from users_mgt import signals
        # from users_mgt import groups
