from django.shortcuts import render, redirect

from .decorators import unauthenticated_user, allowed_users
from .forms import CreateUserForm
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required

@login_required(login_url='login')
def home(request):
    user = request.user
    # Assuming the user is in at least one group
    first_group_name = user.groups.first().name if user.groups.exists() else ""
    context = {
        'user': user,
        'first_group_name': first_group_name,
    }
    return render(request,'accounts/dashboard.html',context=context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def customers(request):
    user = request.user
    first_group_name = user.groups.first().name if user.groups.exists() else ""
    context = {
        'user': user,
        'first_group_name': first_group_name,
    }
    return render(request,'accounts/customers.html',context= context)

@unauthenticated_user
def loginPage(request):
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Username or Password is incorrect')
        
    return render(request,'accounts/login.html')

def logoutPage(request):
    logout(request)
    return redirect('login')
@unauthenticated_user
def register(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    context = {'form':form}
    
    return render(request,'accounts/register.html', context)
#...
#