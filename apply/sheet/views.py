from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib import auth
from django.shortcuts import redirect
from django import forms
from .models import Signup
# Create your views here.
def home(request):
    return render(request, 'index.html')

# def login(request):
#     return render(request, 'login.html')

def signup_page(request):
    if request.method == "POST":

        if request.POST["password"] == request.POST["password2"] and len(request.POST["username"])==9:
            try:
                user = User.objects.create_user(
                    username = request.POST["username"],
                    password = request.POST["password"],
                    email = request.POST["email"],
                )
            
            except:
                return render(request, 'signup.html', {'error':'이미 존재하는 학번입니다.'})

            name = request.POST["name"]
            phone = request.POST["phone"]
            gender = request.POST["gender"]
            major = request.POST["major"]
            signup = Signup(user=user, name=name, phone = phone, gender = gender, major = major)
            signup.save()
            auth.login(request, user)
            return redirect('/')
        else:
            return render(request, 'signup.html', {'error':'학번이 잘못되었거나 비밀번호가 일치하지 않습니다'})
    return render(request, 'signup.html')

def complete(request):
    return render(request, 'complete.html')


def login(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = auth.authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('create')
        else:
            return render(request, 'login.html', {'error':'학번 혹은 패스워드가 틀렸습니다'})
    else:
        return render(request, 'login.html')


def logout(request):
    auth.logout(request)
    return redirect('/')


def profile(request):
    if request.user.is_authenticated: 
        user1 = Signup.objects.get(user = request.user)
        if request.method == "POST":
            if request.POST["password"] != request.POST["password2"]:
                return render(request, 'profile.html', {'error':'비밀번호가 일치하지 않습니다' , 'user1' : user1})
            user1.user.password = request.POST['password']
            user1.user.email = request.POST['email']
            user1.name = request.POST["name"]
            user1.phone = request.POST["phone"]
            user1.gender = request.POST["gender"]
            user1.major = request.POST["major"]
            user1.user.save()
            user1.save()
            return redirect('/')
        
        else:
            return render(request, 'profile.html', {'user1' : user1})
    else:
        return redirect('alert')
