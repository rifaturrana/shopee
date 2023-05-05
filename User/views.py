from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
# Create your views here.

def signup(request):
    if request.method=='POST':
       
        username=request.POST['login_username']
        password=request.POST['login_password']
        print(username,password)
        user=authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            return HttpResponse("User Logged in")
        else:
            if username and password:
                return HttpResponse("User Not Found")
            else:
                username=request.POST['signup_username']
                email=request.POST['signup_email']
                password=request.POST['signup_password']
                password2=request.POST['signup_password2']
                if not username or not email or not password or not password2:
                    return HttpResponse("Fill All Fields")
                if password!=password2:
                    return HttpResponse("Password Not Matched")
                elif User.objects.filter(username=username).exists():
                    return HttpResponse("Username Already Exists")
                elif User.objects.filter(email=email).exists():
                    return HttpResponse("Email Already Exists")
                
                else:
                    user=User.objects.create_user(username,email,password)
                    user.save()
                    return HttpResponse("User Signed Up")
    
    return render(request,'user/signup.html')