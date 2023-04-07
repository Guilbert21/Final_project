from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Profile, feedback



def home(request):
    return render(request, 'templates/index.html')

# def register(request):
#     if request.method=='POST':
#         fname = request.POST.get('fname')
#         lname = request.POST.get('lname')
#         phone = request.POST.get('phone')
#         email = request.POST.get('email')
#         password = request.POST.get('password')

#         new_user = User.objects.create_user(email, password)
#         new_user.first_name = fname
#         new_user.last_name = lname
#         new_user.phone = phone

#         new_user.save()
#         return redirect('login-page')


#     return render(request, 'templates/register.html', {})


def register(request):
    if request.method == 'POST':
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        password = request.POST.get('password')

        # Create a new User instance
        new_user = User.objects.create_user(username=email, email=email, password=password)
        new_user.first_name = fname
        new_user.last_name = lname
        new_user.save()

        profile = Profile.objects.create(user=new_user, first_name=fname, last_name=lname, phone=phone)

        return redirect('login-page')

    return render(request, 'register.html', {})

def error(request):
    return render(request, 'templates/404.html')




def login(request):
    if request.method=='POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = authenticate(request, email=email, password=password)
        if request.user.is_authenticated:
            # login(request, user)
            return redirect('booking-page')    
        else:
            return redirect('error-page')

    return render(request, 'templates/login.html', {} )

def save_feedback(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        feedback.objects.create(name=name, email=email, message=message)
        feedback.save()
        return redirect('home-page')

