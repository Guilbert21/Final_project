from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages


def home(request):
    return render(request, 'templates/index.html')

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            Username = form.cleaned_data.get('Username')
            messages.success(request, f'Account created for {Username}!')
            return redirect('templates/index.html')
    else:
        form = UserCreationForm()

    return render(request, 'templates/register.html')
