from multiprocessing import context
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required

from productos.models import Product, Category


# Create your views here.
@login_required(login_url='login')
def index(request):
    products = Product.objects.select_related("category").all()
    context = {
        'products':products,
        'app_name':'Pablo Store'
    }

    return render(request, 'products/index.html', context)

@login_required(login_url='login')
def detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    context = {
        'product':product,
        'app_name':product.name
    }

    return render(request, 'products/detail.html', context)
@login_required(login_url='login')
def get_products_by_category(request,category_id:int):
    category = Category.objects.prefetch_related('products').get(id=category_id)
    products = category.products.all()

    context = {
        "products":products,
        "category":category,
        "app_name":category.name,
    }

    return render(request, "products/index.html", context)