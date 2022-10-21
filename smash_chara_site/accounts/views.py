from django.shortcuts import render
from .forms import SignupForm, LoginForm
from django.contrib.auth import login
from requests import post
from django.contrib.auth.models import User
from django.views.generic import View, TemplateView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin

class MySignupView(CreateView):
    template_name = 'chara_measures/signup.html'
    form_class = SignupForm
    
    def form_valid(self, form):
        result = super().form_valid(form)
        user = self.object
        login(self.request, user)
        return result

class MyLoginView(LoginView):
    template_name = 'chara_measures/login.html'
    form_class = LoginForm

class MyLogoutView(LogoutView):
    template_name = 'chara_measures/logout.html'

class MyUserView(LoginRequiredMixin, TemplateView):
    template_name = 'chara_measures/mypage.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user
        return context

class MyOtherView(LoginRequiredMixin, TemplateView):
    template_name = 'chara_measures/other.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['users'] = User.objects.exclude(username=self.request.user.username)
        return context