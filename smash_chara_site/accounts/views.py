from re import template
from django.shortcuts import render, redirect
from .forms import SignupForm, LoginForm, PostForm
from django.contrib.auth import login
from requests import post
from chara_measures.models import Post
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.models import User
from django.views.generic import View, TemplateView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin

class MySignupView(CreateView):
    template_name = 'accounts/signup.html'
    form_class = SignupForm
    
    def form_valid(self, form):
        result = super().form_valid(form)
        user = self.object
        login(self.request, user)
        return result

class MyLoginView(LoginView):
    template_name = 'accounts/login.html'
    form_class = LoginForm

class MyLogoutView(LogoutView):
    template_name = 'accounts/logout.html'

class MyPageView(LoginRequiredMixin, TemplateView):
    template_name = 'accounts/mypage.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user
        return context

class MyOtherView(LoginRequiredMixin, TemplateView):
    template_name = 'accounts/other.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['users'] = User.objects.exclude(username=self.request.user.username)
        return context

class CharaMeasuresView(LoginRequiredMixin, TemplateView):
    template_name = 'accounts/measures_list.html'

    # def get(self, request, *args, **kwargs):
    #     measure_data = Post.objects.order_by('-id')
    #     return render(request, 'accounts/measure.html',  {
    #         'measure_data': measure_data
    #     })

class FormView(View):
    form_class = PostForm
    template_name = 'accounts/measures_form.html'

    def get(self, request, *args, **kwargs):
        post_data = PostForm(request.POST or None)
        return render(request, self.template_name,  {
            'post_data': post_data
        })

    def post(self, request, *args, **kwargs):
        form = PostForm(request.POST or None)
        print(form)
        if form.is_valid():
            post_data = PostForm()
            post_data.author = request.user
            post_data.title = form.cleaned_data['title']
            post_data.content = form.cleaned_data['content']
            post_data.save()
            return redirect('chara_measure', post_data.id)
        
        return render(request, 'accounts/measures_form.html', {
            'form':form
        }) 