from announcement_mgt.models import Announcement
# from club_mgt.models import Club
# from users_mgt.models import CustomUser

def generate_announcement(club,user,title,cont):
    Announcement.objects.create(
        club = club,
        author = user,
        title = title,
        contents = cont,
    )
