from django.urls import path
from accounts import views

urlpatterns = [
    path('login/', views.MyLoginView.as_view(), name='account_login'),
    path('logout/', views.MyLogoutView.as_view(), name='account_logout'),
    path('signup/', views.MySignupView.as_view(), name='account_signup'),
    path('mypage/<int:pk>/', views.MyPageView.as_view(), name='mypage'),
    path('mypage/<int:pk>/edit', views.ProfileEditView.as_view(), name='profile_edit'),
    path('chara_measure/<int:pk>/<int:chara_id>/', views.CharaMeasuresView.as_view(), name='chara_measure'),
    path('chara_measure/<int:pk>/<int:chara_id>/measure_form/', views.FormView.as_view(), name='measure_form'),
    path('chara_measure/<int:measure_id>/edit', views.EditView.as_view(), name='measure_edit'),
    path('chara_measure/<int:measure_id>/delete', views.DeleteView.as_view(), name='measure_delete'),
]
