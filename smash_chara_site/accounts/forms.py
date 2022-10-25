from django import forms
from django.contrib.auth.models import User
from .models import AccountUser
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

# class SignupForm(UserCreationForm):
#     class Meta:
#         model = AccountUser
#         fields = ['user_name', 'password1', 'password2']

# class LoginForm(AuthenticationForm):
#     class Meta:
#         model = AccountUser
#         fields = ['username', 'password']

class UserEditForm(forms.ModelForm):
    class Meta:
        model = AccountUser
        fields = [
            'user_name',
        ]

    def __init__(self, user_name=None, *args, **kwargs):
        kwargs.setdefault('label_suffix', '')
        super().__init__(*args, **kwargs)
        # ユーザーの更新前情報をフォームに挿入
        print(user_name)
        if user_name:
            self.fields['user_name'].widget.attrs['value'] = user_name

    def update(self, user):
        user.user_name = self.cleaned_data['user_name']
        user.save()

class PostForm(forms.Form):
    title = forms.CharField(max_length=30, label='タイトル')
    content = forms.CharField(label='内容', widget=forms.Textarea())