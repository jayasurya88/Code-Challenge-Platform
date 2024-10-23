from django.shortcuts import render

# Create your views here.
def index (request):
    return render(request,'index.html')



from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.hashers import make_password
from .models import CustomUser
from django.contrib import messages

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

        # Create and save the user
        user = CustomUser.objects.create(
            first_name=first_name,
            last_name=last_name,
            username=username,
            email=email,
            password=make_password(password)  # Hash the password
        )
        login(request, user)  # Log the user in after successful registration
        return redirect('home')  # Redirect to the home page after registration

    return render(request, 'register.html')






# views.py
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages

def login_view(request):
    if request.method == "POST":
        username_or_email = request.POST.get('username_or_email')
        password = request.POST.get('password')

        # Check if the user exists by username or email
        user = authenticate(request, username=username_or_email, password=password)
        
        if user is not None:
            login(request, user)  # Log the user in
            
            # Check if the user is a superuser
            if user.is_superuser:
                return redirect('admin_dashboard')  # Redirect to the admin page
            else:
                return redirect('index')  # Redirect to the home page for regular users
        else:
            messages.error(request, "Invalid username or password.")
            return render(request, 'login.html')

    return render(request, 'login.html')


def admin_dashboard(request):
    return render(request,"admin_dashboard.html")

from django.contrib.auth import logout
def logout(request):
    logout(request)  # Log the user out
    messages.success(request, "You have been logged out successfully.")
    return redirect('index') 




# views.py
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.contrib import messages
import random
from django.conf import settings
from datetime import timedelta
# To store the generated OTP temporarily
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.hashers import make_password
from django.contrib import messages
from django.core.mail import send_mail
from django.contrib.auth import get_user_model
import random

User = get_user_model()

# Function to generate a random OTP
def generate_otp():
    return str(random.randint(100000, 999999))

# Function to send OTP via email using Django's built-in function
def send_otp_email(email, otp):
    subject = 'Your OTP Code'
    message = f'Your OTP is: {otp}'
    from_email = settings.EMAIL_HOST_USER  # Ensure this is set in your settings
    try:
        send_mail(subject, message, from_email, [email])
    except Exception as e:
        print(f"Failed to send email: {e}")

def password_recovery(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        
        # Check if the email exists in your database
        if User.objects.filter(email=email).exists():
            # Generate and send OTP
            otp = generate_otp()
            send_otp_email(email, otp)

            # Store the OTP and email in the session
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
            return redirect('reset_password')  # Redirect to reset password page
        else:
            messages.error(request, 'Invalid OTP. Please try again.')

    return render(request, 'otp_verification.html')

def reset_password(request):
    if request.method == 'POST':
        new_password = request.POST.get('new_password')
        email = request.session.get('email')  # Get the email from session

        if email:
            # Find the user and reset their password
            user = User.objects.get(email=email)
            user.set_password(new_password)
            user.save()
            messages.success(request, 'Password reset successfully!')
            return redirect('login')  # Adjust according to your URL
        else:
            messages.error(request, 'Email address not found in session.')

    return render(request, 'reset_password.html')
