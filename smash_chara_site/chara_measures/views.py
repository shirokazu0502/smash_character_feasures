from django.shortcuts import render
from django.contrib.auth import login
from requests import post
from django.contrib.auth.models import User
from django.views.generic import View, TemplateView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin

class IndexView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'chara_measures/index.html')
