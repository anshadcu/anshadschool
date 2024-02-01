from django.contrib import messages, auth
from django.contrib.auth.models import User

from django.shortcuts import render, redirect



# Create your views here.
def login (request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')

        else:
            messages.info(request,"invalid credential")
            return redirect('login')
    return render(request,"login.html")
def register(request,):
     if request.method=='POST':
         username=request.POST['username']
         password=request.POST['password']
         conformpassword=request.POST['password1']
         if password==conformpassword:
             if User.objects.filter(username=username).exists():
                 messages.info(request,"Username Taken")
                 return redirect('register')

             else:

                 user=User.objects.create_user(username=username,password=password)

                 user.save();
                 return redirect('login')

         else:
             messages.info(request,"password not matching")
             return redirect('register')
         return redirect('/')
     return render(request,"register.html")
def logout(request):
    auth.logout(request)
    return redirect('/')



def form (request):
    if request.method=='POST':
        name=request.POST['name']
        # age = request.POST['Age']
        # DOB = request.POST['Dateofbirth']
        gender = request.POST['gender']
        email = request.POST['email']
        phonenumber = request.POST['phonenumber']
        # address = request.POST['address']
        # courses = request.POST['courses']
        user=auth.authenticate(name=name, gender=gender, email=email,phonenumber=phonenumber, )
        if user is not None:
            auth.form(request,messages)
            return redirect('/')

        else:
            messages.info(request,"REGISTRATION IS COMPLETED")
            return redirect('form')
    return render(request,"form.html")

def department(request):

    return render(request,"department.html")

