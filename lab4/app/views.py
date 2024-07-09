from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Product,Order,OrderLineItem
from django import forms
from django.contrib.auth.decorators import user_passes_test
# Create your views here.

def home(request):
    return render(request,"home.html")

@login_required
def productList(request):
    products = Product.objects.all()
    return render(request,'productList.html',{'products':products})

@login_required
def addCart(request,pid):
    product = get_object_or_404(Product,pk=pid)
    order,created = Order.objects.get_or_create(user=request.user)
    orderLineItem, created = OrderLineItem.objects.get_or_create(order=order,product=product)
    if not created:
        orderLineItem.qty+=1
        orderLineItem.save()
    return redirect('productList')

@login_required
def viewCart(request):
    order = Order.objects.filter(user=request.user).first()
    if not order:
        order = Order.objects.create(user=request.user)
    return render(request,'viewCart.html',{'order': order})

@login_required
def checkout(request):
    order = Order.objects.filter(user=request.user).first()
    if not order or not order.lineItems.exists():
        return redirect('productList')
    
    if request.method == 'POST':
        for item in order.lineItems.all():
            quantity_key = f'quantity_{item.id}'
            new_quantity = int(request.POST.get(quantity_key, item.qty))
            if new_quantity > 0:
                item.qty = new_quantity
                item.save()
            else:
                item.delete()  # Optional - daca avem qty = 0 ii dam delete 

    return render(request, 'checkout.html', {'order': order})

    return render(request,'checkout.html',{'order': order})


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name','type','description','price']

@user_passes_test(lambda u: u.is_superuser)
def addProduct(request):
    if request.method == "POST":
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('productList')
    else:
        form = ProductForm()
    return render(request,'addProduct.html',{'form':form})