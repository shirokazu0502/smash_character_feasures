from re import template
from django.shortcuts import render, redirect
from .forms import PostForm, UserEditForm
from django.contrib.auth import login
from requests import post
from django.urls import reverse_lazy
from chara_measures.models import Post
from allauth.account import views
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.models import User
from django.views.generic import View, TemplateView, CreateView, FormView
from django.contrib.auth.mixins import LoginRequiredMixin

class MySignupView(views.SignupView):
    template_name = 'accounts/signup.html'
    
    # def form_valid(self, form):
    #     result = super().form_valid(form)
    #     user = self.object
    #     login(self.request, user)
    #     return result

class MyLoginView(views.LoginView):
    template_name = 'accounts/login.html'

class MyLogoutView(views.LogoutView):
    template_name = 'accounts/logout.html'

class MyPageView(LoginRequiredMixin, TemplateView):
    template_name = 'accounts/mypage.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user
        return context

class ProfileEditView(LoginRequiredMixin, FormView):
    template_name = 'accounts/profile.html'
    form_class = UserEditForm
    success_url = reverse_lazy('mypage:pk')
    def form_valid(self, form):
        print(form)
        #formのupdateメソッドにログインユーザーを渡して更新
        form.update(user=self.request.user)
        return super().form_valid(form)

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        print(self.request)
        # 更新前のユーザー情報をkwargsとして渡す
        kwargs.update({
            'user_name' : self.request.user.user_name,
        })
        print(kwargs)
        return kwargs

class MyOtherView(LoginRequiredMixin, TemplateView):
    template_name = 'accounts/other.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['users'] = User.objects.exclude(username=self.request.user.username)
        return context

class CharaMeasuresView(LoginRequiredMixin, TemplateView):
    template_name = 'accounts/measures_list.html'
    def get(self, request, *args, **kwargs):
        print(request.path)
        chara_id=self.kwargs['chara_id'] 
        measure_datas = Post.objects.filter(chara_id=chara_id)
        return render(request, 'accounts/measures_list.html',  {
            'measure_datas': measure_datas,
            'chara_id':chara_id
        })

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
        if form.is_valid():
            pk = self.kwargs['pk']
            chara_id = self.kwargs['chara_id']
            post_data = Post()
            post_data.author = request.user
            post_data.title = form.cleaned_data['title']
            post_data.content = form.cleaned_data['content']
            post_data.chara_id = chara_id
            post_data.save()
            return redirect('chara_measure', pk=pk, chara_id=chara_id)
        
        return render(request, 'accounts/measures_form.html', {
            'form':form
        })

class EditView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        post_data = Post.objects.get(id=self.kwargs['measure_id'])
        print(self.kwargs)
        form = PostForm(
            request.POST or None,
            initial = {
                'title': post_data.title,
                'content': post_data.content
            }
        )

        return render(request, 'accounts/measures_form.html', {
            'form': form
        })

    def post(self, request, *args, **kwargs):
        form = PostForm(request.POST or None)

        if form.is_valid():
            post_data = Post.objects.get(id=self.kwargs['measure_id'])
            post_data.author = request.user
            post_data.title = form.cleaned_data['title']
            post_data.content = form.cleaned_data['content']
            post_data.save()
            return redirect('chara_measure', request.user.pk, post_data.chara_id)
        
        return render(request, 'accounts/measure_form.html', {
            'form':form
        })   

class DeleteView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        print(self.kwargs)
        post_data = Post.objects.get(id=self.kwargs['measure_id'])
        return render(request, 'accounts/measure_delete.html', {
            'post_data': post_data
        })

    def post(self, request, *args, **kwargs):
        post_data = Post.objects.get(id=self.kwargs['measure_id'])
        post_data.delete()
        return redirect('mypage')