
from django.shortcuts import render
from django.contrib.auth import logout, login,authenticate
from django.shortcuts import redirect
from django.contrib.auth.models import User
# Create your views here.
def Logout(request):
    logout(request)
    return redirect('movie')

def Login(request):
    if request.method =="POST":
        Username = request.POST['username']
        Password = request.POST['password']
        user = authenticate(username = Username, password = Password)
        if user is not None:
            login(request, user)
            return redirect('movie')
        else:
            return render(request, 'accounts/login.html',{'error': 'Incorrect username and password.','warning': 'alert alert-danger'})
    return render(request, 'accounts/login.html')

def signup(request):
    if request.method =="POST":
        Username = request.POST['username']
        Password1 = request.POST['password1']
        Password2 = request.POST['password2']
        if Password1 == Password2:
            user = User.objects.create_user(username=Username, password=Password2)
            user.save()
            login(request, user)
            return redirect('movie')

    return render(request, 'accounts/signup.html')