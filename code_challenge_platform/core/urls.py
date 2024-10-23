from django.urls import path,include
from . import views
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('',views.index,name="index"),
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('admin_dashboard/,',views.admin_dashboard, name='admin_dashboard') ,
    path('logout_view/', views.logout_view, name='logout_view'),
    path('password_reset/', views.password_recovery, name='password_reset'),
    
    path('reset_password/', views.reset_password, name='reset_password'),
    path('otp_verification/', views.otp_verification, name='otp_verification'),
    path('profile_view/', views.profile_view, name='profile_view'),
    path('profile_edit/', views.profile_edit, name='profile_edit'),
    
 
    
]