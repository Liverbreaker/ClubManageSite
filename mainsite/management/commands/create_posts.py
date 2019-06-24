import logging

from django.core.management.base import BaseCommand
from announcement_mgt.models import Announcement
from announcement_mgt.setinit import generate_announcement
from club_mgt.models import Club
from users_mgt.models import CustomUser

class Command(BaseCommand):
    help = '建立社團公告範本，請先建立使用者及社團DB'
    def handle(self, *args, **options):
        club_list = ['3D列印社', '羽球社', '熱舞社', '動漫社', '吹玻璃社', '理財投資社', '軟體開發社']
        user = CustomUser.objects.get(username='superman')
        for name in club_list:
            try:
                club = Club.objects.get(name=name)
                generate_announcement(club, user, str("迎新活動 of {}".format(club)), str("{} 將在 2019/10/10~14 舉行迎新活動，請大家踴躍參加!".format(club)))
                generate_announcement(club, user, str("X'mas活動 of {}".format(club)), str("{} 將在 2019/12/30 舉行聖誕晚會，請大家踴躍參加!".format(club)))
                generate_announcement(club, user, str("社團博覽會 of {}".format(club)), str("{} 將在 2019/9/20~24 舉行聖誕集會，請大家踴躍參加!".format(club)))
            except Club.DoesNotExist:
                logging.warning("Club name: {} does not exist".format(name))
                continue

        print("Created sample announcements.")
