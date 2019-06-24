import logging

from django.core.management.base import BaseCommand
from club_mgt.models import Club
from club_mgt.setinit import generate_club

class Command(BaseCommand):
    help = 'Creates read only default permission groups for users'

    def handle(self, *args, **options):

        # add new club if not exist
        new_club, created = Club.objects.get_or_create(name="社團中心")
        if created:
            new_club.name_eng = "Club Manage Center"
            new_club.save()
            generate_club()

    print("Created default Clubs.")
