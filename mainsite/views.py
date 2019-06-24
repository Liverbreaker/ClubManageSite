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
from mainsite import models, forms
from users_mgt.views import AlertView
from users_mgt.views import CheckAuthView

class IndexView(TemplateView):
    template_name = 'index.html'

    def get(self, request):
        return render(request, self.template_name)


class LoginView(auth_views.LoginView):
    template_name = 'login.html'
    success_url = "index"
    def get_context_data(self, *args, **kwargs):
        context = super(LoginView, self).get_context_data(*args, **kwargs)
        # context['messages'] = list(["123","456"])
        return context

class LogoutView(TemplateView):
    def get(self, request):
        auth_logout(request)
        return redirect('logout_redir')

class LogoutRedirectView(AlertView):
    alert = '您已安全登出，是否要重新登入?'

class TestAuthView(CheckAuthView):
    class Meta:
        proxy=True
