from django.db import models
from djrichtextfield.models import RichTextField
from club_mgt.models import Club
from users_mgt.models import CustomUser
from django.utils import timezone
from datetime import datetime, date, time, timedelta
from django.urls import reverse


def days_from_now(delta):
    tt = datetime.today()
    tt = tt.replace(hour=23, minute=59, second=59, microsecond=999999)
    ts = tt+timedelta(days=delta)
    return ts
    # (days=0, seconds=0, microseconds=0, milliseconds=0, minutes=0, hours=0, weeks=0)
    # return timezone.now() + timezone.timedelta(days=delta)

# Create your models here.
class Announcement(models.Model):
    '''公告，包含社團公告及中心公告
    僅有permission者可以發布，幹部/老師 of specific club、社團中心人員'''
    # fs = FileSystemStorage(location='/media/storage/')
    club = models.ForeignKey(Club, verbose_name="社團", on_delete=models.CASCADE)
    author = models.ForeignKey(
        CustomUser, verbose_name="發布人", on_delete=models.CASCADE)
    title = models.CharField(verbose_name="標題", max_length=100)
    contents = RichTextField(verbose_name="內文" )
    # clips = models.FileField(upload_to=fs)
    # https://stackoverflow.com/questions/39576174/save-base64-image-in-django-file-field
    due = models.DateTimeField(verbose_name="到期日", default=days_from_now(60))
    log_add_time = models.DateTimeField(auto_now_add=True)  # log建立時間
    timestamp = models.DateTimeField(auto_now=True)  # 紀錄變更-時間戳記(若有變更)
    is_activate = models.BooleanField(default=True)

    class Meta:
        ordering = ['-timestamp']
        permissions = (
            ("can_view", "Can view Announcement"),
            ("can_add", "Can add Announcement"),
            ("can_edit", "Can edit Announcement"),
            ("can_close", "Can close Announcement"),
            ("can_delete", "Can delete Announcement"),
        )

    def __str__(self):
        strings = [str(self.club), str(self.author), str(self.title)]
        return '$'.join(strings)

    def get_absolute_url(self):
        return reverse('post_detail', kwargs={'pk': self.pk})

    # def get_queryset(self):
    #     default_queryset = super(Announcement,self).get_queryset()
    #     return default_queryset.filter().order_by('-timestamp')
