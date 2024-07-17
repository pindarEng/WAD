from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Product
import json
# Create your views here.

def home(request):
    return render(request,"home.html")

@csrf_exempt
def addProduct(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        name = data.get('name')
        type = data.get('type')
        description = data.get('description')
        price = data.get('price')

        product = Product.objects.create(name=name, type=type, description=description, price=price)
        return JsonResponse({'message': 'Product added successfully.'})

@csrf_exempt
def delete_product(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'DELETE':
        product.delete()
        return JsonResponse({'message': 'Product deleted successfully.'})

@csrf_exempt
def modify_product(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'PUT':
        data = json.loads(request.body)
        product.name = data.get('name')
        product.price = data.get('price')
        product.save()
        return JsonResponse({'message': 'Product modified successfully.'})

@csrf_exempt
def product_list(request):
    products = Product.objects.all()
    return JsonResponse(list(products.values()), safe=False)