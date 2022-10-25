import django
from django.db import models
from django.conf import settings
from django.utils import timezone
from accounts.models import AccountUser
# Create your models here.

class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    chara_id = models.IntegerField("キャラクターid")
    title = models.CharField("タイトル", max_length=200)
    content = models.TextField("本文")

    def __str__(self):
        return self.title    