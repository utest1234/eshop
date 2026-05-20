from email.mime import message
from urllib import request

from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect, render
import urllib

from cart.cart import Cart
from .models import Category, Product
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .forms import RegisterForm, ProductForm

def home(request):
    products = Product.objects.all()
    return render(request, 'home.html', {'products': products})

def about(request):
    return render(request, 'about.html', {})

def products_detail(request, pk):
    product = Product.objects.get(id=pk)
    return render(request, 'product_detail.html', {'product': product})

def category(request, catname):
    catname = urllib.parse.unquote(catname).replace('-', ' ')
    try:
        cat = Category.objects.get(name=catname)
        products = Product.objects.filter(category=cat)
        product_form = ProductForm(initial={'category': cat})
        return render(request, 'category.html', {
            'products': products,
            'category': cat,
            'product_form': product_form,
        })
    except:
        messages.success(request, 'Тохирох ангилал олдсонгүй')
        return redirect('home')

def add_product(request, catname):
    if not request.user.is_authenticated or not request.user.is_staff:
        messages.error(request, 'Зөвхөн админ бүтээгдэхүүн нэмэх боломжтой')
        return redirect('category', catname=catname)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Бүтээгдэхүүн амжилттай нэмэгдлээ!')
        else:
            messages.error(request, 'Мэдээллийг зөв бөглөнө үү.')
    return redirect('category', catname=catname)

def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'Амжилттай нэвтэрлээ')
            return redirect('home')
        else:
            messages.error(request, 'Нэвтрэх нэр эсвэл нууц үг буруу байна')
            return redirect('login')
    else:
        return render(request, 'login.html', {})

def logout_user(request):
    logout(request)
    messages.success(request, 'Амжилттай гарлаа')
    return redirect('home')

def register_user(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Бүртгүүлсэнд баярлалаа. Одоо нэвтэрнэ үү.')
            return redirect('login')
        else:
            messages.error(request, 'Бүртгүүлэхэд алдаа гарлаа. Мэдээллээ шалгаад дахин оролдоно уу.')
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})

def search(request):
    search_value = request.GET.get('searched', '')
    result = []
    if search_value:
        result = Product.objects.filter(name__icontains=search_value)
        if not result:
            messages.success(request, 'Хайлтын үр дүн олдсонгүй')
    return render(request, 'search.html', {'result': result, 'search_value': search_value})

def home(request):
    # Дата баазаас бүх бүтээгдэхүүнийг авна
    products = Product.objects.all() 
    # Хэрэв идэвхтэй барааг шүүх бол: Product.objects.filter(is_active=True)
    
    categories = Category.objects.all() # Дэд цэсэнд харуулах категориуд
    
    context = {
        'products': products,
        'categories': categories,
    }
    return render(request, 'home.html', context)