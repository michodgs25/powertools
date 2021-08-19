from django.shortcuts import get_object_or_404, render

from .models import Category, Product


def product_all(request):
    products = Product.objects.all()
    return render(request, 'store/home.html', {'products': products})
