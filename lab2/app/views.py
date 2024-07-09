from django.shortcuts import render,redirect
from .models import Product,User
from .forms import ProductForm,UserForm
# Create your views here.

def home(request):
    return render(request,"index.html")

def addUser(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('viewUsers')
    else:
        form = UserForm()
    return render(request,'addUser.html',{'form':form})

def viewUsers(request):
    users = User.objects.all()
    return render(request,"viewUsers.html",{'users':users})

def addProduct(request):
    if request.method == "POST":
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("viewProducts")
    else:
        form = ProductForm()
    return render(request,'addProduct.html',{'form':form})

def viewProducts(request):
    products = Product.objects.all()
    return render(request,"viewProducts.html",{'products':products})

def findProducts(request):
    products = Product.objects.none()  # Initialize with an empty QuerySet
    if request.method == "GET":
        category = request.GET.get('category', '').strip()
        min_price = request.GET.get('min_price')
        max_price = request.GET.get('max_price')

        products = Product.objects.all()
        if category:
            products = products.filter(category=category)
        if min_price:
            products = products.filter(price__gte=min_price)
        if max_price:
            products = products.filter(price__lte=max_price)
        
    return render(request, 'findProducts.html', {'products': products})

