import logging

from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group
from django.contrib.auth.models import Permission

# GROUPS = ['admin', 'centermember', 'teacher-mgt', 'teacher-norm', 'student-mgt', 'student-norm']
# MODELS = ['announcement_mgt.announcement', 'activity_mgt.activity', 'activity_mgt.activity_join', 'club_mgt.club', 'club_mgt.member', 'club_mgt.member_quit', 'club_mgt.club_apply', 'club_mgt.club_apply_permit']
# PERMISSIONS = ['view', ]  # For now only view permission by default for all, others include add, delete, change
PERM = {
    "admin": {
        'announcement_mgt.announcement':
            ('view', 'add', 'change', 'close', 'delete'),
        'activity_mgt.activity':
            ('view', 'add', 'change', 'close', 'delete'),
        'activity_mgt.activity_join':
            ('view', 'add', 'change', 'delete'),
        'club_mgt.club':
            ('view', 'add', 'change', 'close', 'delete'),
        'club_mgt.member':
            ('view', 'add', 'change', 'delete'),
        'club_mgt.member_quit':
            ('view', 'add', 'change', 'delete'),
        'club_mgt.club_apply':
            ('view', 'add', 'change', 'delete'),
        'club_mgt.club_apply_permit':
            ('view', 'add', 'change', 'delete')
    },
    "centermember": {
        'announcement_mgt.announcement':
            ('view', 'add', 'change', 'close', 'delete'),
        'activity_mgt.activity':
            ('view', 'add', 'change', 'close', 'delete'),
        'activity_mgt.activity_join':
            ('view', 'add', 'change', 'delete'),
        'club_mgt.club':
            ('view', 'add', 'change', 'close', 'delete'),
        'club_mgt.member':
            ('view', 'add', 'change', 'delete'),
        'club_mgt.member_quit':
            ('view', 'add', 'change', 'delete'),
        'club_mgt.club_apply':
            ('view'),
        'club_mgt.club_apply_permit':
            ('view')
    },
    "teacher-mgt": {
        'announcement_mgt.announcement':
            ('view', 'add', 'change', 'close', 'delete'),
        'activity_mgt.activity':
            ('view', 'add', 'change', 'close', 'delete'),
        'activity_mgt.activity_join':
            ('view', 'add', 'change', 'delete'),
        'club_mgt.club':
            ('view', 'change', 'close'),
        'club_mgt.member':
            ('view', 'add', 'change', 'delete'),
        'club_mgt.member_quit':
            ('view', 'add', 'change', 'delete'),
        'club_mgt.club_apply':
            ('view', 'add', 'change', 'delete'),
        'club_mgt.club_apply_permit':
            ('view', 'add', 'change', 'delete')
    },
    "teacher-norm": {
        'announcement_mgt.announcement':
            ('view'),
        'activity_mgt.activity':
            ('view'),
        'activity_mgt.activity_join':
            ('view', 'add', 'change', 'delete'),
        'club_mgt.club':
            ('view'),
        'club_mgt.member':
            ('view'),
        'club_mgt.member_quit':
            ('view')
    },
    "student-mgt": {
        'announcement_mgt.announcement':
            ('view', 'add', 'change', 'close', 'delete'),
        'activity_mgt.activity':
            ('view', 'add', 'change', 'close', 'delete'),
        'activity_mgt.activity_join':
            ('view', 'add', 'change', 'delete'),
        'club_mgt.club':
            ('view', 'change'),
        'club_mgt.member':
            ('view', 'add', 'change', 'delete'),
        'club_mgt.member_quit':
            ('view', 'add', 'change', 'delete'),
        'club_mgt.club_apply':
            ('view', 'add', 'change', 'delete'),
        'club_mgt.club_apply_permit':
            ('view', 'add', 'change', 'delete')
    },
    "student-norm": {
        'announcement_mgt.announcement':
                ('view'),
            'activity_mgt.activity':
                ('view'),
            'activity_mgt.activity_join':
                ('view', 'add', 'change', 'delete'),
            'club_mgt.club':
                ('view'),
            'club_mgt.member':
                ('view'),
            'club_mgt.member_quit':
                ('view'),
            'club_mgt.club_apply':
                ('view', 'add', 'change', 'delete'),
            'club_mgt.club_apply_permit':
                ('view')
    }
}


class Command(BaseCommand):
    help = 'Creates read only default permission groups for users'
    def handle(self, *args, **options):
        for group in PERM:
            new_group, created = Group.objects.get_or_create(name=group)
            for amodel in PERM[group]:
                app = amodel.split(".")[0]
                model = amodel.split(".")[1]
                if type(PERM[group][amodel]) == str:
                    permission = PERM[group][amodel]
                    name = 'Can {} {}'.format(permission, model)
                    print("Creating {} for {}".format(name, group))
                    try:
                        model_add_perm = Permission.objects.get(name=name)
                    except Permission.DoesNotExist:
                        logging.warning("Permission not found with name '{}'.".format(name))
                        continue
                    new_group.permissions.add(model_add_perm)
                else:
                    for permission in PERM[group][amodel]:
                        name = 'Can {} {}'.format(permission, model)
                        print("Creating {} for {}".format(name, group))
                        try:
                            model_add_perm = Permission.objects.get(name=name)
                        except Permission.DoesNotExist:
                            logging.warning("Permission not found with name '{}'.".format(name))
                            continue
                        new_group.permissions.add(model_add_perm)

        print("Created default group and permissions.")
