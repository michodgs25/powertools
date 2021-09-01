from django.urls import path, include

from . import views

app_name = 'store'

urlpatterns = [
    path('', views.all_products, name='all_products'),
  #  path('', include('home.urls')),
    path('item/<slug:slug>/', views.product_detail, name='product_detail'),
    path('search/<slug:category_slug>/', views.category_list, name='category_list'),
]
