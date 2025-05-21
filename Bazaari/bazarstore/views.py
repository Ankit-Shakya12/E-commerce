from django.shortcuts import render,redirect
from .models import Product,Category
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages

# Create your views here.

def index(request):
    products = Product.objects.all()
    categories = Category.objects.all()
    return render(request,'home.html',{'featured_products':products,'categories':categories})

def login_page(request):
    return render(request,'login.html')

def logout_page(request):
    logout(request)
    messages.success(request,("You have been logged out...."))
    return redirect('home')

def register_page(request):
    return render(request,'register.html')

def dashboard(request):
    return render(request,'dashboard.html')