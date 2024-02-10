from pyexpat.errors import messages
from django.http import HttpResponse
from django.shortcuts import redirect, render

from login.models import User
from .forms import SignUp, LoginForm
from django.contrib.auth import authenticate
# Create your views here.
def index(request):
    return render (request,'home.html')

def login(request):
    form = LoginForm(request.POST or None)
    msg= None
    if request.method =='POST':
        if form.is_valid():
            email = form.cleaned.data.get('email')
            password = form.changed.data.get('password')
            user = authenticate(email=email,password=password)
            if user is not None:
                login(request,user)
                return redirect('index')
            else:
                msg ='invalid credentials'
        else:
            msg='error validating form'
    return render(request,'login.html',{'form':form,'msg':msg})

def register(request):
    msg = None
    if request.method=='POST':
        form = SignUp(request.POST)
        if form.is_valid():
            user =form.save()
            msg ='User Created'
            return redirect('login')
        else:
            msg='form is not valid'
    else:
        form=SignUp()
    return render(request,'register.html',{'form':form,'msg':msg})

def dashboard(request):
    return render (request,'dashboard.html')

def handleSignUp(request):
    if request.method=="POST":
        # Get the post parameters
        username=request.POST['username']
        email=request.POST['email']
        fname=request.POST['fname']
        lname=request.POST['lname']
        pass1=request.POST['pass1']
        pass2=request.POST['pass2']

        if len(username)<10:
            messages.error(request, " Your user name must be under 10 characters")
            return redirect('home')

        if not username.isalnum():
            messages.error(request, " User name should only contain letters and numbers")
            return redirect('home')
        if (pass1!= pass2):
             messages.error(request, " Passwords do not match")
             return redirect('home')
        
        # check for errorneous input
        
        # Create the user
        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name= fname
        myuser.last_name= lname
        myuser.save()
        messages.success(request, " Your User has been successfully created")
        return redirect('index')
    else:
        return HttpResponse("404 - Not found")
    
def handeLogin(request):
     if request.method=="POST":
        # Get the post parameters
             loginusername=request.POST['loginusername']
             loginpassword=request.POST['loginpassword']

             user=authenticate(username= loginusername, password= loginpassword)
             if user is not None:
                 login(request, user)
                 messages.success(request, "Successfully Logged In")
                 return redirect("home")
             else:
               messages.error(request, "Invalid credentials! Please try again")
     return redirect("home")