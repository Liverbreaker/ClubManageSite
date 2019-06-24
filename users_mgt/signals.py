# from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone

from .models import CustomUser, Student, Teacher, CenterMember
from club_mgt.models import Member, Club


@receiver(post_save, sender=CustomUser)
def create_profile(sender, instance, created, **kwargs):
    if created:
        if instance.user_type == "STUDENT":
            Student.objects.create(
                user=instance, nickname=instance.get_full_name())
            # instance.Student.save()
        elif instance.user_type == "TEACHER":
            Teacher.objects.create(
                user=instance, nickname=instance.get_full_name(), position="教師")
            # instance.Teacher.save()
        elif instance.user_type == "CENTERMEMBER":
            CenterMember.objects.create(
                user=instance, nickname=instance.get_full_name(), position="社團中心成員")
            try:
                new_club, created = Club.objects.get_or_create(name="社團中心")
                if created:
                    new_club.name_eng = "Club Manage Center"
                    new_club.save()
                    generate_club()
            except Club.DoesNotExist:
                raise ValueError('Club does not exist, pass by users_mgt/signals.py')
            Member.objects.create(user=instance,
                                  club=new_club,
                                  is_manage=True,
                                  position="社團中心老師",
                                  club_enterday=timezone.now()
                                  )
        else:
            raise ValueError(
                'UserManager error, create user with empty user_type.')

# @receiver(post_save, sender=CustomUser)
# def save_profile(sender, instance, **kwargs):
#     instance.save()
