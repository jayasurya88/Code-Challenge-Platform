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