from django.shortcuts import render

def login(request):
    context = {}
    return render(request, 'accounts/login.html')

def signup(request):
    context = {}
    return render(request, 'accounts/signup.html')