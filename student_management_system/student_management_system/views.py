from django.shortcuts import render,redirect,HttpResponse
from student_management_app.EmailBackEnd import EmailBackEnd
from django.contrib import messages
from django.contrib.auth import authenticate,logout,login
from django.contrib.auth.decorators import login_required
from student_management_app.models import CustomUser
@login_required
def BASE(request):
    return render(request, 'base.html')


def LOGIN(request):
    return render(request,'login.html')

def dologin(request):
    if request.method=="POST":
        user=EmailBackEnd.authenticate(request,username=request.POST.get('email'),password=request.POST.get('password'))
        if user!=None:
            login(request,user)
            user_type=user.user_type
            if user_type=='1':
                return redirect('home')
            elif user_type=='2':
                return redirect('manager_home')
            elif user_type=='3':
                return redirect("Employee_home")
            else:
                messages.error(request,'Email and password are incorrect')
                return redirect('login')
        else:
            messages.error(request,'Email and password are incorrect')
            return redirect('login')
@login_required        
def doLogout(request):
    logout(request)
    return redirect('login')

@login_required(login_url='/')
def PROFILE(request):
    user=CustomUser.objects.get(id=request.user.id)
    context={
        'user':user,
    }
    return render(request,'profile.html',context)
@login_required(login_url='/')
def PROFILE_UPDATE(request):
    if request.method=="POST":
        first_name=request.POST.get('firstname')
        last_name=request.POST.get('lastname')
        official_email=request.POST.get('off_email')
        username=request.POST.get('username')
        password=request.POST.get('password')
        print(first_name,last_name,username)
        
        try:
            customeuser=CustomUser.objects.get(id=request.user.id)
            customeuser.first_name=first_name
            customeuser.last_name=last_name
            if password != None and password!="":
                customeuser.set_password(password)
            customeuser.save()
            messages.success(request,'Your Profile is updated')
            redirect('profile')
        except:
            messages.error(request,'Error in updating profile')

    return render(request,'profile.html')


