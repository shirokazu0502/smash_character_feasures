from django.urls import path
from accounts import views

urlpatterns = [
    path('login/', views.MyLoginView.as_view(), name='login'),
    path('logout/', views.MyLogoutView.as_view(), name='logout'),
    path('signup/', views.MySignupView.as_view(), name='signup'),
    path('mypage/<int:pk>/', views.MyPageView.as_view(), name='mypage'),
    path('chara_measure/<int:chara_id>/', views.CharaMeasuresView.as_view(), name='chara_measure'),
    path('chara_measure/<int:chara_id>/measure_form/', views.FormView.as_view(), name='measure_form'),
]
