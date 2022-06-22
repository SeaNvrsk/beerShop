from django.contrib.auth import views
from django.urls import path

urlpatterns = [
    path('accounts/login/', views.LoginView.as_view(), name='login'),
    path('accounts/logout/', views.LogoutView.as_view(), name='logout'),
    path('accounts/password-reset/', views.PasswordResetView.as_view(), name='password_reset'),
    path('accounts/password-reset/done/', views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('accounts/reset/<uidb64>/<token>/', views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('accounts/reset/done/', views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    path('accounts/password-change/', views.PasswordChangeView.as_view(), name='password_change'),
    path('accounts/password-change/done/', views.PasswordChangeDoneView.as_view(), name='password_change_done'),
    ]