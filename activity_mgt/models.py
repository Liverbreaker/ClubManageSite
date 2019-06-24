from django.db import models
from club_mgt.models import Member, Club
from users_mgt.models import Student, Teacher
from djrichtextfield.models import RichTextField

# Create your models here.
class Activity(models.Model):
    '''社團舉辦的活動，所有學生都能參加'''
    name = models.CharField(max_length=200)  # 活動名稱
    begin = models.DateTimeField(auto_now=False)  # 起始時日
    end = models.DateTimeField(auto_now=False)  # 終了時日
    deadline = models.DateTimeField(auto_now=False)  # 報名截止時日
    principal = models.ForeignKey(Member, on_delete=models.CASCADE)  # 活動負責人學號
    club = models.ForeignKey(Club, on_delete=models.CASCADE)  # 主辦社團
    content = RichTextField()  # 活動內容
    site = models.CharField(max_length=40)  # 活動場地
    contact = models.TextField()  # 聯絡方式
    fee = models.IntegerField()  # 參加費用
    meal = models.BooleanField(default=False)  # 是否供餐
    insure = models.BooleanField(default=True)  # 是否保險
    note = RichTextField()  # 備註
    log_add_time = models.DateTimeField(auto_now_add=True)  # 活動紀錄建立時間
    timestamp = models.DateTimeField(auto_now=True)  # 活動內容變更-時間戳記
    is_activate = models.BooleanField(default=True)

    class Meta:
        ordering = ['-timestamp']
        permissions = (
            ("can_view", "Can view Activity"),
            ("can_add", "Can add Activity"),
            ("can_edit", "Can edit Activity"),
            ("can_close", "Can close Activity"),
            ("can_delete", "Can delete Activity"),
        )

    def __str__(self):
        return self.name


class Activity_join(models.Model):
    '''學生報名社團舉辦的活動的紀錄'''
    act_id = models.ForeignKey(Activity, on_delete=models.CASCADE)  # 參加的活動
    attender = models.ForeignKey(Student, on_delete=models.CASCADE)  # 參加人
    email = models.CharField(max_length=50)  # email
    phone = models.CharField(max_length=12)  # 手機
    log_add_time = models.DateTimeField(auto_now_add=True)  # 活動紀錄建立時間
    timestamp = models.DateTimeField(auto_now=True)  # 活動內容變更-時間戳記

    class Meta:
        ordering = ['-timestamp']
        permissions = (
            ("can_view", "Can view Activity_join"),
            ("can_add", "Can add Activity_join"),
            ("can_edit", "Can edit Activity_join"),
            ("can_delete", "Can delete Activity_join"),
        )

    def __str__(self):
        strings = [self.act_id, self.attender]
        return '$'.join(strings)
