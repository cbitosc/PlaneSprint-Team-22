from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required(login_url='signup')
def HomePage(request):
    return render (request,'main.html')
def SignupPage(request):
    if(request.method=='POST'):
        uname=request.POST.get('username')
        email=request.POST.get('email')
        pass1=request.POST.get('password1')
        pass2=request.POST.get('password2')
        if(pass1!=pass2):
            return redirect('signup')
        my_user=User.objects.create_user(uname,email,pass1)
        my_user.save()
        return redirect ('login')
    return render (request,'signup.html')
def LoginPage(request):
    if(request.method=='POST'):
        username=request.POST.get('username')
        pass1=request.POST.get('pass')
        print(username,pass1)
        user=authenticate(request,username=username,password=pass1)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            return redirect('login')
           
    return render (request,'login.html')
def LogOut(request):
    logout(request)
    return redirect ('login')
@login_required(login_url='signup')
def CoursesPage(request):
    return render (request,'courses.html')
@login_required(login_url='signup')
def ReviewsPage(request):
    return render (request,'reviews.html')
@login_required(login_url='signup')
def TeachersPage(request):
    return render (request,'teacher.html')
@login_required(login_url='signup')
def maincoursePage(request):
    return render (request,'main_course.html')
@login_required(login_url='signup')
def section1Page(request):
    return render (request,'section1.html')


