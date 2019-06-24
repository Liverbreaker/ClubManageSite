from django.db import models
from users_mgt.models import CustomUser, Student, Teacher, CenterMember
from djrichtextfield.models import RichTextField

class Club(models.Model):
    name = models.CharField(max_length=20, verbose_name="社團名字(中文)", unique=True)  # 社團名字(中文)
    name_eng = models.CharField(
        max_length=50, verbose_name="社團名字(英文)", blank=True, null=True, unique=True)  # 社團名字(英文)
    leader = models.ForeignKey("users_mgt.Student", on_delete=models.CASCADE,
                               verbose_name="社長", blank=True, null=True)  # 學生學號(負責人)
    teacher = models.ForeignKey("users_mgt.Teacher", on_delete=models.CASCADE,
                                verbose_name="指導老師", blank=True, null=True)  # 教師編號(指導老師)
    manager = models.ForeignKey("users_mgt.CustomUser", on_delete=models.CASCADE,
                                verbose_name="社團中心負責人", blank=True, null=True)  # 社團中心負責人
    office = models.CharField(
        max_length=15, verbose_name="社辦", blank=True, null=True)  # 社團辦公室
    activity_place = models.CharField(
        max_length=50, blank=True, null=True, verbose_name="活動地點")  # 活動地點
    fee = models.IntegerField(blank=True, null=True, verbose_name="社費")  # 社費
    activity_time = models.TextField(
        blank=True, null=True, verbose_name="活動時間")  # 活動時間
    web = models.CharField(max_length=100, blank=True,
                           null=True, verbose_name="粉專連結")  # 粉專連結
    contact = models.TextField(
        blank=True, null=True, verbose_name="聯絡資訊")  # 聯絡資訊
    info = RichTextField(blank=True, null=True, verbose_name="社團簡介")  # 社團簡介
    log_add_time = models.DateTimeField(auto_now_add=True)  # 紀錄建立時間
    timestamp = models.DateTimeField(auto_now=True)  # 紀錄時間戳記
    is_activate = models.BooleanField(default=True, verbose_name="社團運作中")

    class Meta:
        ordering = ['-timestamp']
        permissions = (
            ("can_view", "Can view Club"),
            ("can_add", "Can add Club"),
            ("can_edit", "Can edit Club"),
            ("can_close", "Can close Club"),
            ("can_delete", "Can delete Club"),
        )

    def __str__(self):
        # return "_".join([self.name, self.timestamp])
        return self.name

class Member(models.Model):
    '''加入社團log: include 學生/教師/社團中心負責人'''
    user = models.ForeignKey(
        "users_mgt.CustomUser", on_delete=models.CASCADE, verbose_name="成員名稱")
    club = models.ForeignKey(
        Club, on_delete=models.CASCADE, verbose_name="所屬社團")  # 社團or單位
    is_manage_stu = models.BooleanField(verbose_name="是否為幹部(學生)", default=False)  # True=是幹部
    is_manage = models.BooleanField(verbose_name="是否為指導老師", default=False)  # True=是幹部
    position = models.CharField(
        max_length=10, null=True, blank=True, verbose_name="幹部職稱")  # 是幹部，職稱?(可空)
    club_enterday = models.DateField(verbose_name="入社日期")  # 入社日期
    log_add_time = models.DateTimeField(auto_now_add=True)  # 紀錄建立時間
    timestamp = models.DateTimeField(auto_now=True)  # 紀錄時間戳記

    class Meta:
        ordering = ['-timestamp']
        permissions = (
            ("can_view", "Can view Member"),
            ("can_add", "Can add Member"),
            ("can_edit", "Can edit Member"),
            ("can_delete", "Can delete Member"),
        )

    def __str__(self):
        # print("{username}-{club}".format(username=self.user.username, club=self.club.name))
        return "{username}-{club}".format(username=self.user.username, club=self.club.name)
        # return self.user.name

    def __clubname__(self):
        return self.club.name

    def __club__(self):
        return self.club


class Member_quit(models.Model):
    '''學生退出社團log'''
    member = models.OneToOneField(
        Member, on_delete=models.CASCADE, verbose_name="學生")
    quitday = models.DateField(
        blank=True, null=True, verbose_name="退社日期")  # 退社日期
    log_add_time = models.DateTimeField(auto_now_add=True)  # 紀錄建立時間
    timestamp = models.DateTimeField(auto_now=True)  # 紀錄時間戳記

    class Meta:
        ordering = ['-timestamp']
        permissions = (
            ("can_view", "Can view Member_quit"),
            ("can_add", "Can add Member_quit"),
            ("can_edit", "Can edit Member_quit"),
            ("can_delete", "Can delete Member_quit"),
        )

    def __str__(self):
        # strings = [self.member.name, self.member.studentID, self.member.club.name, str(self.quitday)]
        strings = [self.member.student.name,
                   self.member.club.name, str(self.quitday)]
        return '$'.join(strings)

class Club_apply(models.Model):
    '''學生加入/退出社團申請書'''
    student = models.ForeignKey("users_mgt.Student", on_delete=models.CASCADE)  # 學生學號
    club = models.ForeignKey(Club, on_delete=models.CASCADE)  # 申請社團
    IO_CHOICES = ((True, '入社'), (False, '退社'))
    in_out = models.BooleanField(verbose_name="申請入社or退社", choices=IO_CHOICES, default=True)
    reason = RichTextField(blank=False, null=False)  # 申請原因說明
    text1 = models.TextField(blank=True, null=True)  # 其他欄位1
    text2 = models.TextField(blank=True, null=True)  # 其他欄位2
    bool1 = models.BooleanField()  # 布林值1
    bool2 = models.BooleanField()  # 布林值2
    # text1, text2, bool1, bool2 作為各社團申請書中的自定義項(例如填入推薦人，或是否參與比賽...)
    log_add_time = models.DateTimeField(auto_now_add=True)  # log建立時間
    timestamp = models.DateTimeField(auto_now=True)  # 紀錄變更-時間戳記(若有變更)
    BOOL_CHOICES = ((True, '是'), (False, '否'))
    is_permitted = models.BooleanField(verbose_name="是否通過申請?", choices=BOOL_CHOICES, default=False) #是否已經處理過

    class Meta:
        ordering = ['-timestamp']
        permissions = (
            ("can_view", "Can view Club_apply"),
            ("can_add", "Can add Club_apply"),
            ("can_edit", "Can edit Club_apply"),
            ("can_delete", "Can delete Club_apply"),
        )

    def __str__(self):
        strings = [self.student, self.club]
        return '$'.join(strings)


class Club_apply_permit(models.Model):
    '''學生加入/退出社團之申請書---學生幹部/老師 許可'''
    apply_id = models.OneToOneField(
        Club_apply, on_delete=models.CASCADE)  # 申請書編號
    permitter = models.ForeignKey(
        "users_mgt.CustomUser", on_delete=models.CASCADE)  # 審核人
    RES_BOOL = ((True, '通過'), (False, '不通過'))
    result = models.BooleanField(choices=RES_BOOL)  # 審核結果
    log_add_time = models.DateTimeField(auto_now_add=True)  # log建立時間
    timestamp = models.DateTimeField(auto_now=True)  # 紀錄變更-時間戳記(若有變更)

    class Meta:
        ordering = ['timestamp']
        permissions = (
            ("can_view", "Can view Club_apply_permit"),
            ("can_add", "Can add Club_apply_permit"),
            ("can_edit", "Can edit Club_apply_permit"),
            ("can_delete", "Can delete Club_apply_permit"),
        )

    def __str__(self):
        strings = [self.apply_id, self.permitter]
        return '$'.join(strings)
