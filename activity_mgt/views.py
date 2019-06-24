from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404, HttpResponseRedirect
# from django.contrib import messages
from django.contrib.auth import (authenticate, login as auth_login,
                                 logout as auth_logout)
from django.views.generic import (TemplateView, DetailView, ListView,
                                  FormView, CreateView, UpdateView, DeleteView)
# from django.utils.decorators import method_decorator
# from django.contrib.auth.decorators import login_required
# @login_required is only for def() functions
from django.db import IntegrityError
from .models import Activity
from .forms import ActivityForm
from mainsite.views_mixin import LoginRequiredMixin
# from mysystem import settings
from django.urls import reverse_lazy
from django.utils import timezone
# from club_mgt.models import Member, Club
# from announcement_mgt.models import days_from_now

# Create your views here.
class ActivityListView(LoginRequiredMixin, ListView):
    '''社團活動清單'''
    template_name = 'activity_list.html'
    model = Activity
    # context_object_name = 'announcement_list'

    def get_context_data(self):
        qs = Activity.objects.filter(begin__lte=timezone.now())
        context = super().get_context_data()
        context['title'] = "社團活動管理系統"
        context['subtitle'] = "社團活動"
        if qs != []:
            context['act_list'] = qs
        return context

class ActivityDetailView(LoginRequiredMixin, DetailView):
    '''社團活動內容'''
    template_name = 'activity_add.html'
    form_class = ActivityForm
    

class ActivityCreateView(LoginRequiredMixin, CreateView):
    '''社團活動創建'''
    template_name = 'activity_add.html'
    form_class = ActivityForm
    def get_initial(self, *args, **kwargs):
        initial = super(ActivityCreateView, self).get_initial(**kwargs)
        # initial['deadline'] = days_from_now(60)
        return initial

    def get_form_kwargs(self):
        kwargs = super(ActivityCreateView, self).get_form_kwargs()
        kwargs['request'] = self.request
        return kwargs

    def form_valid(self, form):
        form.instance.author = self.request.user
        try:
            return super(ActivityCreateView, self).form_valid(form)
        except IntegrityError as e:
            form.add_error("title", e)
            return self.form_invalid(form)

    def get_context_data(self, *args, **kwargs):
        context = super(ActivityCreateView,
                        self).get_context_data(**kwargs)
        context['title'] = "社團管理系統"
        context['subtitle'] = "社團公告"
        context['subtitle_sub'] = "新增公告"
        # context['form'].fields['club'].queryset = get_all_club(self) #moved to forms.py
        return context

class ActivityEditView(LoginRequiredMixin, UpdateView):
    '''社團活動內容編輯'''
    template_name = 'activity_list.html'
    model = Activity
    # return render()

class ActivityComfirmDeleteView(LoginRequiredMixin, DeleteView):
    '''社團活動刪除'''
    template_name = 'activity_list.html'
    model = Activity
    # return render()

class ActivityComfirmCloseView(LoginRequiredMixin, DeleteView):
    '''社團活動確認關閉(結束)
    BTN FROM DetailView Comfirm close'''
    template_name = 'activity_list.html'
    model = Activity
    # return render()

# class ActivitySignupView(LoginRequiredMixin, CreateView):
#     '''報名參加:activity_join'''
#     return True
#
# class ActivitySignedListView(LoginRequiredMixin, ListView):
#     '''已報名 活動清單'''
#
# class ActivitySignedDetailView(LoginRequiredMixin, DetailView):
#     '''已報名活動 報名表內容'''
#
# class ActivitySignedEditView(LoginRequiredMixin, UpdateView):
#     '''已報名活動 變更報名表'''
#
# class ActivitySignedDeleteView(LoginRequiredMixin, DeleteView):
#     '''已報名活動 取消報名'''
#
# class ActivitySignedAllListView(LoginRequiredMixin, ListView):
#     '''報名表總覽
#     is提出報名表的club, is std-mgt or is tea-mgt,
#     '''
#
# class ActivitySignedAllDeleteView(LoginRequiredMixin, DeleteView):
#     '''報名表總覽
#     剔除報名'''
