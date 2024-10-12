from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.template import loader
from django.http import HttpResponse
from django.contrib.auth import authenticate,login,logout
from django.views.decorators.cache import cache_control
# Create your views here.
def user_register(request):
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = User.objects.filter(username=username)

        if user.exists():
            messages.info(request,'User with this username already exists try different username')
            return redirect("/auth/register/")
        
        user = User.objects.create_user(username=username)

        user.set_password(password)

        user.save()
        
        messages.info(request,'User created successfully')
        return redirect('/auth/login/')
    
    template = loader.get_template('register.html')
    context = {}
    return HttpResponse(template.render(context,request))
    
    
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def user_login(request):
            
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        if not User.objects.filter(username=username).exists():
            messages.info(request,'User with this username does not exist')
            return redirect('/auth/login/')
        
        user = authenticate(username=username, password=password)

        if user is None:
            messages.info(request,'invalid password please try again!')
            return redirect('/auth/login')
        

        login(request,user)
        messages.info(request,'login successful')
        return redirect('/add/list')
        #return redirect('/home')
    
    template = loader.get_template('loginx.html')
    context ={}
    return HttpResponse(template.render(context,request))

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def user_logout(request):
    logout(request)
    messages.info(request,"logged out")
    return redirect("/auth/login")

    
