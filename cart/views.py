from django.shortcuts import render
from django.shortcuts import get_object_or_404


from .cart import Cart


def cart_summary(request):
    return render(request, 'store/cart/summary.html')


def cart_add(request):
    cart = Cart(request)
    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('productid'))
        product = get_object_or_404(Product, id=product_id)
        cart.add(product=product)


    return render(request, 'store/cart/cart_add')