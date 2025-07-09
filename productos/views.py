from multiprocessing import context
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

from productos.models import Product, Category


# Create your views here.
def index(request):
    products = Product.objects.select_related("category").all()
    context = {
        'products':products
    }

    return render(request, 'products/index.html', context)


def detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    context = {
        'product':product
    }

    return render(request, 'products/detail.html', context)

def get_products_by_category(request,category_id:int):
    category = Category.objects.prefetch_related('products').get(id=category_id)
    products = category.products.all()

    context = {
        "products":products,
        "category":category
    }

    return render(request, "products/category.html", context)