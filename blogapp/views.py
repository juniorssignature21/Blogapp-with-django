from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
# Create your views here.

def home(request):
    return render(request, 'blogapp/home.html')

def register_user(request):
    if request.method == "POST":
        get_name = request.POST.get('name')
        get_email = request.POST.get('email')
        get_password= request.POST.get('pass1')
        get_confirmpassword= request.POST.get('pass2')
        
        if get_password != get_confirmpassword:
            messages.warning(request, "Passwords Mismatch")
            return redirect('/signup')
        query = User.objects.create_user(get_email, get_email, get_password)
        query.save()
        
        query=authenticate(username=get_email, password=get_password)
        if query is not None:
            login(request, query)
            messages.success(request, "User Created & Login Successful")
            return redirect('/')
        
    return render(request, 'blogapp/register.html')

def login_user(request):
    if request.method == "POST":
        get_email = request.POST.get('email')
        get_password= request.POST.get('pass1')
            
        myuser = authenticate(username=get_email, password=get_password)
        if myuser is not None:
            login(request, myuser)
            messages.success(request, "Login Successful")
            return redirect('/')
        else:
            messages.warning(request, "Invalid credentials")
            return redirect('/login')
        
    return render(request, "blogapp/login.html")
            
            
def logout_user(request):
    logout(request)
    messages.success(request, "Logout Success")
    return redirect('/')