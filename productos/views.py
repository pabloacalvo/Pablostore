from multiprocessing import context
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required, permission_required
from .forms import CommentForm

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
    product = Product.objects.prefetch_related('comments__user').get(id=product_id)
    comments = product.comments.order_by('-created_at').all()
    form = CommentForm()
    context = {
        'product':product,
        'app_name':product.name,
        'form':form,
        'comments':comments,
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

@login_required
@permission_required("products.add_comment", raise_exception=True)
def comment_view(request, product_id):
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            comment.product = Product.objects.get(id=product_id)
            print(form.cleaned_data)
            comment.save()

    return redirect('detail', product_id=product_id)