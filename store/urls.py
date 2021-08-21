from django.urls import path

from . import views

app_name = 'store'

urlpatterns = [
    path('', views.product_all, name='product_all'),
    path('item/<slug:slug>/', views.product_detail, name='product_detail'),
]
