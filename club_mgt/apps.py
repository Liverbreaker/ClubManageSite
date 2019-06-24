from django.apps import AppConfig


class ClubMgtConfig(AppConfig):
    name = 'club_mgt'

    def ready(self):
        # pass
        from club_mgt import signals
        
