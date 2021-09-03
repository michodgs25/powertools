from django.shortcuts import render


def cart_summary(request):
    return render(request, 'store/cart/summary.html')
