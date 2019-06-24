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
from .models import Announcement
from .forms import AnnouncementForm
from mainsite.views_mixin import LoginRequiredMixin
# from mysystem import settings
from django.urls import reverse_lazy
from django.utils import timezone
from club_mgt.models import Member, Club
from announcement_mgt.models import days_from_now

class AnnouncementListView(LoginRequiredMixin, ListView):
    '''公告清單'''
    template_name = 'announcement_list.html'
    model = Announcement
    # context_object_name = 'announcement_list'

    def get_context_data(self):
        qs = Announcement.objects.filter(due__gte=timezone.now())
        context = super().get_context_data()
        context['title'] = "社團管理系統"
        context['subtitle'] = "社團公告"
        if qs != []:
            context['announcement_list'] = qs
        return context

class AnnouncementCreateView(LoginRequiredMixin, CreateView):
    '''公告新建'''
    template_name = 'announcement_add.html'
    form_class = AnnouncementForm

    def get_initial(self, *args, **kwargs):
        initial = super(AnnouncementCreateView, self).get_initial(**kwargs)
        initial['due'] = days_from_now(60)
        return initial

    def get_form_kwargs(self):
        kwargs = super(AnnouncementCreateView, self).get_form_kwargs()
        kwargs['request'] = self.request
        return kwargs

    def form_valid(self, form):
        form.instance.author = self.request.user
        try:
            return super(AnnouncementCreateView, self).form_valid(form)
        except IntegrityError as e:
            form.add_error("title", e)
            return self.form_invalid(form)

    def get_context_data(self, *args, **kwargs):
        context = super(AnnouncementCreateView,
                        self).get_context_data(**kwargs)
        context['title'] = "社團管理系統"
        context['subtitle'] = "社團公告"
        context['subtitle_sub'] = "新增公告"
        # context['form'].fields['club'].queryset = get_all_club(self) #moved to forms.py
        return context


class AnnouncementDetailView(LoginRequiredMixin, DetailView):
    '''公告內容'''
    template_name = 'announcement_detail.html'
    model = Announcement

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['form'].fields['author'].initial = self.request.user.name
        context['title'] = "社團管理系統"
        context['subtitle'] = "社團公告"
        context['subtitle_sub'] = "公告內容:title"
        context['mypost'] = Announcement.objects.get(
            pk=self.kwargs['pk'])
        return context


class AnnouncementEditView(LoginRequiredMixin, UpdateView):
    '''公告編輯'''
    template_name = 'announcement_edit.html'
    model = Announcement
    form_class = AnnouncementForm
    # fields = ['title','contents', 'due']
    pk_url_kwargs = 'post_pk'
    context_object_name = 'post'
    def get_form_kwargs(self):
        kwargs = super(AnnouncementEditView, self).get_form_kwargs()
        kwargs['request'] = self.request
        return kwargs
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['title'] = "社團管理系統"
        context['subtitle'] = "社團公告"
        context['mypost'] = Announcement.objects.get(
            pk=self.kwargs['pk'])
        return context

    def form_valid(self, form):
        form.instance.author = self.request.user
        if self.request.POST.get('button') == 'cancel':
            return HttpResponseRedirect(self.get_success_url())
        elif self.request.POST.get('button') == 'submit':
            try:
                return super(AnnouncementEditView, self).form_valid(form)
            except IntegrityError as e:
                # form.add_error("title", e)
                return self.form_invalid(form)
        else:
            raise ValueError("Error posting announcement")


class AnnouncementDeleteView(LoginRequiredMixin, DeleteView):
    '''公告刪除'''
    template_name = 'announcement_comfirm_delete.html'
    model = Announcement
    success_url = reverse_lazy('post_list')
    def get_context_data(self, *args, **kwargs):
        context = super(AnnouncementDeleteView, self).get_context_data(*args, **kwargs)
        context['title'] = "社團管理系統"
        context['subtitle'] = "社團公告"
        return context

    # below:: delete button not solved!!!
    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        success_url = self.get_success_url()
        self.object.delete()
        return redirect(success_url)

    # def form_valid(self, form):
    #     if 'cancel' in self.request.POST:
    #         return HttpResponseRedirect(self.get_success_url())
    #     elif self.request.POST.get('button') == 'submit':
    #         try:
    #             return super(AnnouncementDeleteView, self).form_valid(form)
    #         except IntegrityError as e:
    #             # form.add_error("title", e)
    #             return self.form_invalid(form)
    #     else:
    #         raise ValueError("Error posting announcement")
    #
    # def post(self, request, *args, **kwargs):
    #     if "cancel" in request.POST:
    #         url = self.get_success_url()
    #         return HttpResponseRedirect(url)
    #     else:
    #         return super(AnnouncementDeleteView, self).post(request, *args, **kwargs)
