from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
# Create your views here.

def signup(request):
    if request.method=='POST':
       is_login=request.POST["is_login"]
       if is_login=="1":
            username=request.POST['login_username']
            password=request.POST['login_password']
            print(username,password)
            user=authenticate(username=username,password=password)
            if user is not None:
                login(request,user)
                return redirect('home')
            else:
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
                return redirect('signup')
    return render(request,'user/signup.html')


def signout(request):
    logout(request)
    return redirect('signup')

def home(request):
     if request.user.is_authenticated:
        return render(request,'home/index.html',{'user':request.user})
     return redirect('signup')

def user_profile(request):
     if request.user.is_authenticated:
        return render(request,'user/user_profile.html',{'user':request.user})
     return redirect('signup')