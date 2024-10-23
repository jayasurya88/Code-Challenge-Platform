from django.urls import path,include
from . import views
urlpatterns = [
    path('',views.index,name="index"),
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('admin_dashboard/,',views.admin_dashboard, name='admin_dashboard') ,
    path('logout/', views.logout, name='logout'),
]