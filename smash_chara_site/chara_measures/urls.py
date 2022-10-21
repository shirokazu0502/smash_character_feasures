from django.urls import path
from chara_measures import views

urlpatterns = [
    path("", views.IndexView.as_view(), name="smash_site_home"),
    path("signup/", views.MySignupView.as_view(), name="signup"),
    path("mypage/<int:pk>/", views.MyUserView.as_view(), name="mypage"),
    path("login/", views.MyLoginView.as_view(), name="login"),
    path("logout/", views.LogoutView.as_view(), name="logout"),
]