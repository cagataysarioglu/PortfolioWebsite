from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .models import Product, Category

def index(request):
    products = Product.objects.all()
    categories = Category.objects.all()
    context = {
        'products': products,
        'categories': categories
    }
    return render(request, "products/list.html", context)

def detail(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    context = {
        'product': product
    }
    return render(request, "products/detail.html", context)

def search(request):
    return render(request, "products/search.html")
