from django import forms
from .models import Activity
from django.forms.models import ModelChoiceField
from djrichtextfield.widgets import RichTextWidget
# from mainsite.widgets import BootstrapDateTimePickerInput
from mainsite.widgets import XDSoftDateTimePickerInput
# from django.contrib.admin.widgets import AdminDateWidget
from club_mgt.models import Member, Club


class ActivityForm(forms.ModelForm):
    # 
    club = ModelChoiceField(label='舉辦單位', queryset=None)
    begin = forms.DateTimeField(label="活動起始日", input_formats=[
                              '%Y/%m/%d %H:%M'], widget=XDSoftDateTimePickerInput())
    end = forms.DateTimeField(label="活動終止日", input_formats=[
                              '%Y/%m/%d %H:%M'], widget=XDSoftDateTimePickerInput())
    deadline = forms.DateTimeField(label='報名截止時日', input_formats=[
                              '%Y/%m/%d %H:%M'], widget=XDSoftDateTimePickerInput())
    principal = ModelChoiceField(label='活動負責人', queryset=None)
    content = forms.CharField(label='內容', widget=RichTextWidget())
    site = forms.CharField(label='場地')
    contact = forms.CharField(label='聯絡方式', widget=RichTextWidget())
    fee = forms.IntegerField(label='參加費用',)
    meal = forms.BooleanField(label='是否供餐',)
    insure = forms.BooleanField(label='是否有保險',)
    note = forms.CharField(label='備註', widget=RichTextWidget())

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request')
        super(ActivityForm, self).__init__(*args, **kwargs)
        def get_all_member(self):
            membersets = Member.objects.filter(user=self.request.user)
            return membersets
        def get_all_club(self):
            clubsets = Club.objects.filter(member__in=get_all_member(self))
            return clubsets
        try:
            self.fields['club'].queryset = get_all_club(self)
            self.fields['principal'].queryset = get_all_member(self)
        except:
            # print(get_all_club(self))
            raise ValueError('activity_mgt.forms.py crash: choice club')

        


    class Meta:
        model = Activity
        fields = ['club', 
        'begin', 
        'end', 
        'deadline', 
        'principal', 
        'content', 
        'site', 
        'contact', 
        'fee',
        'meal', 
        'insure', 
        'note',]
        exclude = ('author',)
