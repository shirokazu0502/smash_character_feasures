from django.urls import path
from chara_measures import views

urlpatterns = [
    path("", views.IndexView.as_view(), name="smash_site_home"),
]