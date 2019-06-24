from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
# from django.contrib.auth.models import Group
from django.utils.translation import ugettext_lazy as _
from django.conf import settings
from .forms import CustomUserChangeForm, CustomUserCreationForm
from .models import CustomUser, Student, Teacher, CenterMember
from club_mgt.models import Club
from users_mgt.models import CustomGroup, CustomPermission, CustomContentType

from django.contrib.auth.models import Group, Permission

# @admin.register(CustomGroup)
# class CustomGroupAdmin(admin.ModelAdmin):
#     # list_display = ['name', 'permissions',]
#     class Meta:
#         proxy=True
#
# @admin.register(CustomPermission)
# class CustomPermissionAdmin(admin.ModelAdmin):
#     list_display = ('name', 'content_type', 'codename',)

# Group.permissions.set()

# admin.site.unregister(Group)
# admin.site.unregister(Permission)
# admin.site.unregister(ContentType)
# admin.site.register(CustomGroup, CustomGroupAdmin)
# admin.site.register(CustomPermission, CustomPermissionAdmin)


# --------------------------------------------
from club_mgt.models import Member, Member_quit
class MemberQuitInline(admin.StackedInline):
    model = Member_quit
class MemberInline(admin.StackedInline):
    model = Member
    inlines = [MemberQuitInline]
    verbose_name_plural = 'members'
# --------------------------------------------
class CenterMemberInline(admin.StackedInline):
    model = CenterMember
    verbose_name_plural = 'CenterMember'
    verbose_name_plural = 'CenterMembers'

class StudentInline(admin.StackedInline):
    model = Student
    verbose_name_plural = 'student'
    verbose_name_plural = 'students'

class TeacherInline(admin.StackedInline):
    model = Teacher
    verbose_name_plural = 'teacher'
    verbose_name_plural = 'teachers'
# --------------------------------------------

class ClubInline(admin.StackedInline):
    model = Club


@admin.register(CustomUser)
class CustomUserAdmin(BaseUserAdmin):
    form = CustomUserChangeForm
    add_form = CustomUserCreationForm
    # change_password_form =
    model = CustomUser
    list_display = ('username', 'email', 'user_type', 'is_activate', 'date_joined',)
    list_filter = ('is_superuser', 'is_activate', 'user_type', 'groups')
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (_('Personal info'), {'fields': ('last_name',
                                         'first_name', 'email', 'avatar', 'user_type')}),
        (_('Permissions'), {'fields': ('is_active',
                                       # 'is_staff',
                                       'is_superuser',
                                       'groups', 'user_permissions')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'password1', 'password2'),
        }),
    )
    search_fields = ('username', 'full_name', 'email',)
    ordering = ('username',)
    filter_horizontal = ('groups', 'user_permissions',)
    inlines = [StudentInline, TeacherInline, CenterMemberInline, MemberInline]

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('user', 'nickname', 'major', 'grade')
    # inlines = [MemberInline]

@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ('user', 'nickname', 'position')
    # inlines = [MemberInline]

@admin.register(CenterMember)
class CenterMemberAdmin(admin.ModelAdmin):
    list_display = ('user', 'nickname', 'position')
    # inlines = [MemberInline]
