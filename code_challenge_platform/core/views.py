from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.hashers import make_password
from .models import CustomUser
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib.auth.models import User
from django.core.mail import send_mail
import random
from django.conf import settings
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth import get_user_model
import random


def index (request):
    return render(request,'index.html')



def register(request):
    if request.method == "POST":
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        if password != confirm_password:
            messages.error(request, "Passwords do not match.")
            return render(request, 'registration/register.html')

        if CustomUser.objects.filter(username=username).exists():
            messages.error(request, "Username already exists.")
            return render(request, 'registration/register.html')

        if CustomUser.objects.filter(email=email).exists():
            messages.error(request, "Email already exists.")
            return render(request, 'registration/register.html')

        
        user = CustomUser.objects.create(
            first_name=first_name,
            last_name=last_name,
            username=username,
            email=email,
            password=make_password(password)  
        )
        login(request, user)  
        return redirect('home')  

    return render(request, 'register.html')


def login_view(request):
    if request.method == "POST":
        username_or_email = request.POST.get('username_or_email')
        password = request.POST.get('password')
        user = authenticate(request, username=username_or_email, password=password)
        
        if user is not None:
            login(request, user)  
            
            if user.is_superuser:
                return redirect('admin_dashboard')  
            else:
                return redirect('index')  
        else:
            messages.error(request, "Invalid username or password.")
            return render(request, 'login.html')

    return render(request, 'login.html')


def admin_dashboard(request):
    return render(request,"admin_dashboard.html")


def logout(request):
    logout(request)  
    messages.success(request, "You have been logged out successfully.")
    return redirect('index') 






User = get_user_model()

def generate_otp():
    return str(random.randint(100000, 999999))

def send_otp_email(email, otp):
    subject = 'Your OTP Code'
    message = f'Your OTP is: {otp}'
    from_email = settings.EMAIL_HOST_USER  
    try:
        send_mail(subject, message, from_email, [email])
    except Exception as e:
        print(f"Failed to send email: {e}")

def password_recovery(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        
        
        if User.objects.filter(email=email).exists():
            otp = generate_otp()
            send_otp_email(email, otp)
            request.session['otp'] = otp
            request.session['email'] = email
            messages.success(request, 'An OTP has been sent to your email.')
            return redirect('otp_verification')
        else:
            messages.error(request, 'Email address not found.')
    return render(request, 'password_reset.html')

def otp_verification(request):
    if request.method == 'POST':
        user_otp = request.POST.get('otp')
        stored_otp = request.session.get('otp')
        if user_otp == stored_otp:
            messages.success(request, 'OTP verified successfully!')
            return redirect('reset_password')  
        else:
            messages.error(request, 'Invalid OTP. Please try again.')
    return render(request, 'otp_verification.html')

def reset_password(request):
    if request.method == 'POST':
        new_password = request.POST.get('new_password')
        email = request.session.get('email')  
        if email:
            
            user = User.objects.get(email=email)
            user.set_password(new_password)
            user.save()
            messages.success(request, 'Password reset successfully!')
            return redirect('login')  
        else:
            messages.error(request, 'Email address not found in session.')

    return render(request, 'reset_password.html')
