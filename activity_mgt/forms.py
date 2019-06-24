from django import forms
from .models import Activity
from django.forms.models import ModelChoiceField
from djrichtextfield.widgets import RichTextWidget
# from mainsite.widgets import BootstrapDateTimePickerInput
from mainsite.widgets import XDSoftDateTimePickerInput
# from django.contrib.admin.widgets import AdminDateWidget
from club_mgt.models import Member, Club

class ActivityForm(forms.ModelForm):
    # 新增活動
    club = ModelChoiceField(label='舉辦單位', queryset=None)
    title = forms.CharField(label='標題')
    contents = forms.CharField(label='內容', widget=RichTextWidget())
    due = forms.DateTimeField(label="活動日期", input_formats=[
                              '%Y/%m/%d %H:%M'], widget=XDSoftDateTimePickerInput())
    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request')
        super(ActivityForm, self).__init__(*args, **kwargs)

        def get_all_club(self):
            membersets = Member.objects.filter(user=self.request.user)
            clubsets = Club.objects.filter(member__in=membersets)
            return clubsets
        try:
            self.fields['club'].queryset = get_all_club(self)
        except:
            # print(get_all_club(self))
            raise ValueError('announcement_mgt.forms.py crash: choice club')

    class Meta:
        model = Activity
        fields = ['club', 'title', 'contents', 'due']
        exclude = ('author',)

class ActivitySignForm(forms.ModelForm):
    # 報名活動
    