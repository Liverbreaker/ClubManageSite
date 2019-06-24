from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, ReadOnlyPasswordHashField
from .models import CustomUser
from django.utils.translation import ugettext_lazy as _
# from django.forms.models import ModelChoiceField
# from djrichtextfield.widgets import RichTextWidget

class CustomUserCreationForm(UserCreationForm):
    username = forms.CharField(label="校園編號")
    email = forms.EmailField(label='電子信箱')
    first_name = forms.CharField(label='名字')
    last_name = forms.CharField(label='姓氏')
    # avatar = forms.ImageField(label='頭像(非必要)')
    password1 = forms.CharField(label='密碼', widget=forms.PasswordInput)
    password2 = forms.CharField(label='請再次輸入密碼', widget=forms.PasswordInput)

    class Meta(UserCreationForm):
        model = CustomUser
        fields = ['username', 'email', 'first_name', 'last_name','user_type']

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("前後輸入的密碼不相符")
        return password2

    def save(self, commit=True):
        # raise forms.ValidationError("signup save failed")
        user = super(CustomUserCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user

class CustomUserChangeForm(UserChangeForm):
    password = ReadOnlyPasswordHashField()
    class Meta(UserChangeForm):
        model = CustomUser
        fields = ['email', 'password',]

    def clean_password(self):
        return self.initial["password"]
