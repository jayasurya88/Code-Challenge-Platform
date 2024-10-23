from django.urls import path,include
from . import views
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('',views.index,name="index"),
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('admin_dashboard/,',views.admin_dashboard, name='admin_dashboard') ,
    path('logout/', views.logout, name='logout'),
    path('password_reset/', views.password_recovery, name='password_reset'),
    
    path('reset_password/', views.reset_password, name='reset_password'),
    path('otp_verification/', views.otp_verification, name='otp_verification'),
    
    
 
    
]