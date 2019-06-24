# from django.core.files.storage import FileSystemStorage
from django.db import models
# from djrichtextfield.models import RichTextField
from django.urls import reverse
from django.contrib.auth.models import PermissionsMixin, AbstractUser, Group, Permission
from django.contrib.contenttypes.models import ContentType
from django.utils.translation import ugettext_lazy as _
from django.core import mail
from .managers import UserManager

# Create your models here.
class CustomUser(AbstractUser, PermissionsMixin):
    User_type_choices = (
        ("STUDENT", "Student"),
        ("TEACHER", "Teacher"),
        ("CENTERMEMBER", "CenterMember")
    )
    username = models.CharField(
        _('ID number'), max_length=15, unique=True)  # 學校編號取代username
    email = models.EmailField(_('email address'), unique=True)
    first_name = models.CharField(_('first name'), max_length=30, blank=True)
    last_name = models.CharField(_('last name'), max_length=30, blank=True)
    # date_joined = models.DateTimeField(_('date joined'), auto_now_add=True)
    is_activate = models.BooleanField(_('activate'), default=True)
    avatar = models.ImageField(_('avatar'), upload_to="avatars/", null=True, blank=True)
    user_type = models.CharField(_('user type'),
        max_length=20, choices=User_type_choices, default="STUDENT")  # 類型(學生/教師/社團中心管理人員)
    is_superuser = models.BooleanField(_('superuser'), default=False)
    is_staff = models.BooleanField(_('staff'), default=False)

    objects = UserManager()

    # USERNAME_FIELD = 'username'  # only numbers
    REQUIRED_FIELDS = ['email', 'user_type', 'first_name', 'last_name']

    class Meta:
        verbose_name = ('user')
        verbose_name_plural = _('users')

    def get_full_name(self):
        full_name = "%s %s" % (self.last_name, self.first_name)
        return full_name.strip()

    def get_short_name(self):
        return self.last_name

    def send_emailto_user(self, subject, message, from_email=None, **kwargs):
        mail.message.send(subject, message, from_email, [self.email], **kwargs)

    def __str__(self):
        return self.username

class Student(models.Model):
    '''註冊類別是學生的USER，附加的個人資訊'''
    grade_choices = (
        ("1", "大一"),
        ("2", "大二"),
        ("3", "大三"),
        ("4", "大四"),
        ("5", "碩一"),
        ("6", "碩二"),
        ("7", "碩三"),
    )
    major_choices = (
        ("管理學院", (
            ("mba", "企管系"),
            ("acct", "會計系"),
            ("stat", "統資系"),
            ("fib", "金企系"),
            ("im", "資管系"),
            )
        ),
        ("管理學院", (
            ("english", "英文系"),
            ("de", "德語系"),
            ("fren", "法文系"),
            ("span", "西文系"),
            ("jp", "日文系"),
            ("italy", "義文系"),
            ("giccs", "跨文化研究所"),
            )
        ),
    )
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    nickname = models.CharField(max_length=20)
    major = models.CharField(max_length=10, choices=major_choices)  # 科系
    grade = models.CharField(max_length=5, choices=grade_choices)  # 年級
    mclass = models.CharField(max_length=5)  # 班級
    log_add_time = models.DateTimeField(auto_now_add=True)  # 紀錄建立時間
    timestamp = models.DateTimeField(auto_now=True)  # 紀錄時間戳記

    def __str__(self):
        return self.nickname

class Teacher(models.Model):
    '''註冊類別是教師的USER，附加的個人資訊'''
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    nickname = models.CharField(max_length=20)
    position = models.CharField(max_length=10)  # 職位
    log_add_time = models.DateTimeField(auto_now_add=True)  # 紀錄建立時間
    timestamp = models.DateTimeField(auto_now=True)  # 紀錄時間戳記

    def __str__(self):
        return self.nickname

class CenterMember(models.Model):
    '''註冊類別是社團中心管理人的USER，附加的個人資訊'''
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    nickname = models.CharField(max_length=20)
    position = models.CharField(max_length=10, blank=True, null=True)  # 職位
    log_add_time = models.DateTimeField(auto_now_add=True)  # 紀錄建立時間
    timestamp = models.DateTimeField(auto_now=True)  # 紀錄時間戳記

    def __str__(self):
        return self.nickname


class CustomGroup(Group):
    class Meta:
        proxy = True


class CustomPermission(Permission):
    class Meta:
        proxy = True


class CustomContentType(ContentType):
    class Meta:
        proxy = True
