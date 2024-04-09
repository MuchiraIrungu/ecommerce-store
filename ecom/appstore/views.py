from django.shortcuts import render,redirect
from .models import Product, Category
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .forms import SignUpForm
from django import forms
from  cart.views import cart_summary

def category(request,foo):
   # replace hyphens with spaces
    foo = foo.replace('-','')
   # grab category from url
    try:
        #look up the category
        category = Category.objects.get(name=foo)
        products = Product.objects.filter(category=category)
        return render(request, 'category.html', {'products':products, 'category':category})


    except:
        messages.success(request, ('Category does not exist'))
        return redirect('home')
			
        

def product(request,pk):
    product = Product.objects.get(id=pk)
    return render(request, 'product.html', {'product':product})



def home(request):
    products = Product.objects.all()
    return render(request, 'home.html', {'products':products})


def about(request):
    return render(request, 'about.html', {})

def login_user(request):
    if request.method == "POST":
        username= request.POST['username']
        password = request.POST['password']
        user =authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request,('login sucesssful'))
            return redirect('home')
        else:
            return render(request, 'login.html', {})


    else:
         return render(request, 'login.html', {})
         

def logout_user(request):
    logout(request)
    messages.success(request, ("logout successful...)"))

    return redirect('login')



def register_user(request):
    form = SignUpForm()
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            #log in user
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, ('You have  registered successfully'))
            return redirect('login')
        
        else:
            messages.success(request, ('Registration unsuccessful '))
            return redirect('register')
			
    else:
        return render(request, 'register.html',{'form':form})
    

 