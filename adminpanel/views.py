from django.shortcuts import render
from django.contrib.auth import authenticate,login as authlogin,logout as authlogout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect,HttpResponse
from django.views.decorators.cache import never_cache

# Create your views here.


@login_required(login_url='logout')
def home(request):
    return render(request,'adminpanel/home.html')


@never_cache
def login(request):
    if request.POST:
        username       =request.POST.get('username')
        password    =request.POST.get('password') 

   
        user=authenticate(username=username,password=password)
        if user:
            # if user.user_type !="Admin":
            #     messages.error(request,"Invalid Admin Credentials")
            # else:
                authlogin(request,user)
                return redirect('home')
        else:
            messages.error(request,"Invalid credentials")
        
    return render(request,'adminpanel/login.html')




def logout(request):
    authlogout(request)
    return redirect('login')