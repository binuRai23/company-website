from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login
from django.contrib import messages
import stripe
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from .models import Enroll
from .forms import EnrollmentForm
from django.core.mail import send_mail
from .signals import create_user_and_send_email
# from django.utils.crypto import get_random_string


def enroll(request):
    if request.method == 'POST':
        form = EnrollmentForm(request.POST)
        
        if form.is_valid():
            form.save()
       
    else:
        form = EnrollmentForm()
 
    return render(request, 'course.html', {'form': form})
    return render(request, 'enrollment_success.html')
    # return HttpResponse('your login credentials has been sent to your email')
    # return redirect('enrollment_success')

def enrollment_success(request):
    return render(request, 'enrollment_success.html')

def Home(request):
    return render(request, 'home.html')

def Course(request):
    return render(request, 'course.html')

def dashboard(request):
    return render(request, 'Sdashboard.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect('Sdashboard.html')
        else:
            messages.error(request, 'Invalid username or password')
            return redirect('login')
    return render(request, 'login.html')
