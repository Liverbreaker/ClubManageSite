from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404, HttpResponseRedirect
# from django.contrib import messages
from django.contrib.auth import (authenticate, login as auth_login,
                                 logout as auth_logout,
                                 forms as auth_forms,
                                 views as auth_views)
from django.contrib.auth.decorators import login_required
from django.views.generic import (TemplateView, DetailView, ListView,
                                  FormView, CreateView, UpdateView)
from django.utils.decorators import method_decorator
from django.urls import reverse_lazy

from ClubManageSite import settings
from mainsite.views_mixin import LoginRequiredMixin
from users_mgt import models, forms

class SignupUserView(CreateView):
    template_name = 'form_signup.html'
    form_class = forms.CustomUserCreationForm
    success_url = reverse_lazy('signup_success')
    def form_valid(self, form):
        try:
            return super().form_valid(form)
        except Exception as e:
            form.add_error('password2', e)
            return self.form_invalid(form)
            # raise ValueError(e)

class AlertView(TemplateView):
    template_name = 'alert.html'
    alert = 'This is as alert!'
    def get_context_data(self, *args, **kwargs):
        context = super(AlertView, self).get_context_data(*args, **kwargs)
        context['myalert'] = self.alert
        return context

class SignupSuccessView(AlertView):
    alert = '嗨，您已成功註冊，請使用註冊帳號登入，謝謝'

class AccountView(LoginRequiredMixin, TemplateView):
    template_name = 'account.html'

    def get(self, request):
        if request.user.is_authenticated:
            return render(request, self.template_name)
        else:
            return redirect('/%s?next=%s' % (settings.LOGIN_URL, request.path))

class CheckAuthView(LoginRequiredMixin, TemplateView):
    template_name = "alert.html"
    def get_context_data(self, *args, **kwargs):
        context = super(CheckAuthView, self).get_context_data(*args, **kwargs)
        # has_perm 會從 cache 找 user 的資料，若要即時顯示改變要先刪除cache
        if self.request.user.has_perm("announcement.can_add"):
            context["myalert"] = "announcement.can_add VVV"
        else:
            context["myalert"] = "announcement.can_add XXX"
        return context
