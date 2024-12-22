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
from .models import Challenge

from django.contrib.auth.decorators import login_required
from django.utils.dateparse import parse_date

def index (request):
    return render(request,'index.html')
def home (request):
    return render(request,'home.html')

def register_view(request):
    return render (request,"register.html")

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
        return redirect('login_view')  

    return render(request, 'register.html')

def login_view(request):
    return render(request,"login.html")
def login1(request):
    if request.method == "POST":
        username_or_email = request.POST.get('username_or_email')
        password = request.POST.get('password')
        user = authenticate(request, username=username_or_email, password=password)
        
        if user is not None:
            login(request, user)  
            
            if user.is_superuser:
                return redirect('admin_dashboard')  
            else:
                return redirect('home')  
        else:
            messages.error(request, "Invalid username or password.")
            return render(request, 'login.html')

    return render(request, 'login.html')


def admin_dashboard(request):
    return render(request,"admin_dashboard.html")



from django.shortcuts import render, redirect
from .models import Challenge, TestCase  # Make sure you have the TestCase model imported
def add_challenge(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        difficulty = request.POST.get('difficulty')
        input_format = request.POST.get('input_format')
        output_format = request.POST.get('output_format')
        examples = request.POST.get('examples')
        template_code = request.POST.get('template_code')  # New field

        # Create and save a new Challenge object
        new_challenge = Challenge(
            title=title,
            description=description,
            difficulty=difficulty,
            input_format=input_format,
            output_format=output_format,
            examples=examples,
            template_code=template_code  # Save the template_code
        )
        new_challenge.save()  # Save the challenge first to get an ID for the test cases

        # Loop through the input test cases and expected outputs
        test_case_count = 1
        while True:
            input_key = f'input_test_case_{test_case_count}'
            expected_key = f'expected_output_test_case_{test_case_count}'
            if input_key not in request.POST or expected_key not in request.POST:
                break  # Exit loop if no more test cases are found

            input_data = request.POST.get(input_key)
            expected_output = request.POST.get(expected_key)

            # Create and save each test case
            TestCase.objects.create(
                challenge=new_challenge,
                input_data=input_data,
                expected_output=expected_output
            )
            test_case_count += 1  # Move to the next test case number

        return redirect('admin_dashboard')  # Redirect to the admin dashboard after adding

    return render(request, 'admin_add_challenge.html')


def logout_view(request):
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
            return redirect('login1')  
        else:
            messages.error(request, 'Email address not found in session.')

    return render(request, 'reset_password.html')






@login_required
def profile_edit(request):
    user = request.user

    if request.method == "POST":
        user.first_name = request.POST.get('first_name', '')
        user.last_name = request.POST.get('last_name', '')
        user.gender = request.POST.get('gender', '')
        user.location = request.POST.get('location', '')

        birthday_input = request.POST.get('birthday', '').strip()
        if birthday_input:
            user.birthday = parse_date(birthday_input)
            if user.birthday is None:
                messages.error(request, "Invalid date format. Use YYYY-MM-DD.")
                return render(request, 'profile_edit.html', {'user': user})
        else:
            user.birthday = None

        user.skills = request.POST.get('skills', '')

        if request.FILES.get('profile_picture'):
            user.profile_picture = request.FILES['profile_picture']

        user.save()
        messages.success(request, "Profile updated successfully!")
        return redirect('profile_view')

    context = {
        'user': user
    }
    return render(request, 'profile_edit.html', context)


    context = {
        'user': user
    }
    return render(request, 'profile_edit.html', context)


def profile_view(request):
    user = request.user
    return render(request, 'profile_view.html', {'user': user})




# views.py
from django.shortcuts import render, get_object_or_404
from django.shortcuts import render
from .models import Challenge

def challenge_list(request):
    challenges = Challenge.objects.all()  # Fetch all Challenge objects
    return render(request, 'challenge_list.html', {'challenges': challenges})


def challenge_detail(request, id):
    challenge = get_object_or_404(Challenge, id=id)
    test_cases = challenge.test_cases.all()  # Retrieve related test cases
    return render(request, 'challenge_detail.html', {
        'challenge': challenge,
        'test_cases': test_cases,  # Pass test cases to the template
    })

def take_challenge(request, id):
    challenge = get_object_or_404(Challenge, id=id)
    return render(request, 'take_challenge.html', {'challenge': challenge})




# Edit Challenge
@login_required
def edit_challenge(request, challenge_id):
    challenge = get_object_or_404(Challenge, id=challenge_id)

    if request.method == 'POST':
        challenge.title = request.POST.get('title')
        challenge.description = request.POST.get('description')
        challenge.difficulty = request.POST.get('difficulty')
        challenge.input_format = request.POST.get('input_format')
        challenge.output_format = request.POST.get('output_format')
        challenge.examples = request.POST.get('examples')
        challenge.template_code = request.POST.get('template_code')
        challenge.save()

        # Update existing test cases
        for test_case in challenge.test_cases.all():
            input_data = request.POST.get(f"input_test_case_{test_case.id}")
            expected_output = request.POST.get(f"expected_output_test_case_{test_case.id}")
            if input_data and expected_output:
                test_case.input_data = input_data
                test_case.expected_output = expected_output
                test_case.save()

        # Handle new test cases
        new_test_case_id = 1
        while request.POST.get(f"input_test_case_new_{new_test_case_id}"):
            input_data = request.POST.get(f"input_test_case_new_{new_test_case_id}")
            expected_output = request.POST.get(f"expected_output_test_case_new_{new_test_case_id}")
            if input_data and expected_output:
                TestCase.objects.create(challenge=challenge, input_data=input_data, expected_output=expected_output)
            new_test_case_id += 1

        messages.success(request, "Challenge updated successfully!")
        return redirect('admin_dashboard')  # Redirect to admin dashboard

    context = {'challenge': challenge}
    return render(request, 'admin_edit_challenge.html', context)

# Delete Challenge
@login_required
def delete_challenge(request, challenge_id):
    challenge = get_object_or_404(Challenge, id=challenge_id)
    
    if request.method == 'POST':
        challenge.delete()
        messages.success(request, "Challenge deleted successfully!")
        return redirect('admin_dashboard')  # Redirect to admin dashboard

    context = {
        'challenge': challenge
    }
    return render(request, 'admin_delete_challenge.html', context)


def admin_challenge_list(request):
    challenges = Challenge.objects.all()  # Fetch all challenges from the database
    return render(request, 'admin_challenge_list.html', {'challenges': challenges})
# rohit code         756e517a77msh58ac762d967fff7p128ae3jsnc233287d404d
#jayasurya           8ede8ff6dcmshcc206ea377c20c6p1db6bfjsnd3bcd1169d5e
# editor/views.py
import requests
import base64
from django.shortcuts import render
from django.http import JsonResponse

# List of RapidAPI keys
RAPIDAPI_KEYS = [
    "756e517a77msh58ac762d967fff7p128ae3jsnc233287d404d",
    "8ede8ff6dcmshcc206ea377c20c6p1db6bfjsnd3bcd1169d5e",
    
    
]

# Track usage per key
key_usage = {key: 0 for key in RAPIDAPI_KEYS}
DAILY_LIMIT = 100  # Example daily limit per key
current_key_index = 0  # Start with the first key

API_HOST = "judge0-ce.p.rapidapi.com"



# In views.py
from django.shortcuts import render, get_object_or_404
from .models import Challenge
def get_rapidapi_key():
    global current_key_index
    key = RAPIDAPI_KEYS[current_key_index]
    
    # Check if the current key has reached its limit
    if key_usage[key] >= DAILY_LIMIT:
        current_key_index = (current_key_index + 1) % len(RAPIDAPI_KEYS)
        key = RAPIDAPI_KEYS[current_key_index]
    
    return key
 
def code_editor(request, challenge_id):
    challenge = get_object_or_404(Challenge, id=challenge_id)
    context = {
        "challenge": challenge,
        "template_code": challenge.template_code 
    }
    return render(request, "code_editor.html", context)


# editor/views.py
# editor/views.py

LANGUAGE_IDS = {
    "cpp": 52,         # C++
    "python": 71,      # Python
    "java": 62,        # Java
    "javascript": 63   # JavaScript
}



def submit_code(request, challenge_id):
    if request.method == "POST":
        user = request.user  # Get the currently logged-in user
        challenge = get_object_or_404(Challenge, id=challenge_id)
        source_code = request.POST.get("source_code")
        language = request.POST.get("language")

        if language not in LANGUAGE_IDS:
            return JsonResponse({"error": "Unsupported language"}, status=400)

        # Retrieve all test cases for the challenge
        test_cases = challenge.test_cases.all()
        results = []
        all_passed = True  # Track if all test cases pass

        for test_case in test_cases:
            payload = {
                "language_id": LANGUAGE_IDS[language],
                "source_code": base64.b64encode(source_code.encode("utf-8")).decode("utf-8"),
                "stdin": base64.b64encode(test_case.input_data.encode("utf-8")).decode("utf-8"),
                "base64_encoded": "true"
            }

            key = get_rapidapi_key()
            headers = {
                "x-rapidapi-key": key,
                "x-rapidapi-host": API_HOST,
                "Content-Type": "application/json"
            }

            response = requests.post(f"https://{API_HOST}/submissions", json=payload, headers=headers)

            # Log the response and increment usage
            print("Submission API response:", response.json())
            if response.status_code == 201:
                token = response.json().get("token")
                key_usage[key] += 1
                result = get_result(token)

                print("Result object:", result)
                output, error_output, compile_output = decode_outputs(result)
                expected_output = test_case.expected_output.strip() if test_case.expected_output else ""

                if error_output:
                    status = "Runtime Error"
                    all_passed = False  # Mark as not fully passed
                elif compile_output:
                    status = "Compilation Error"
                    all_passed = False
                elif output.strip() == expected_output:
                    status = "Accepted"
                else:
                    status = "Wrong Answer"
                    all_passed = False

                results.append({
                    "input": test_case.input_data,
                    "expected": expected_output,
                    "output": output,
                    "status": status
                })
            else:
                results.append({"error": "Code submission failed."})
                all_passed = False

        # Award points if all test cases are passed
        if all_passed:
            # Define point system based on challenge difficulty
            difficulty_points = {
                "Easy": 10,
                "Medium": 20,
                "Hard": 30,
            }
            points = difficulty_points.get(challenge.difficulty, 0)

            # Add points to the user
            if hasattr(user, "add_points"):
                user.add_points(points)
                return JsonResponse({"results": results, "points_awarded": points})
            else:
                return JsonResponse({"results": results, "error": "User model does not support points."}, status=400)

        return JsonResponse({"results": results, "points_awarded": 0})

    return JsonResponse({"error": "Invalid request method"}, status=405)

def get_result(token):
    key = get_rapidapi_key()
    headers = {
        "x-rapidapi-key": key,
        "x-rapidapi-host": API_HOST
    }
    params = {"base64_encoded": "true"}  
    response = requests.get(f"https://{API_HOST}/submissions/{token}", headers=headers, params=params)

    # Log the response and increment usage
    print("Get result API response:", response.json())
    if response.status_code == 200:
        key_usage[key] += 1
    return response.json()

def decode_outputs(result):
    
    try:
        output = base64.b64decode(result.get("stdout", "")).decode("utf-8") if result.get("stdout") else "No output"
        error_output = base64.b64decode(result.get("stderr", "")).decode("utf-8") if result.get("stderr") else None
        compile_output = base64.b64decode(result.get("compile_output", "")).decode("utf-8") if result.get("compile_output") else None
    except Exception as e:
        # Log any decoding exceptions
        print("Decoding error:", e)
        output = "Failed to decode output"
        error_output = None
        compile_output = None
    
    return output, error_output, compile_output



def add_padding(b64_string):
    
    if b64_string:
        missing_padding = len(b64_string) % 4
        if missing_padding:
            b64_string += '=' * (4 - missing_padding)
    return b64_string

