from django.shortcuts import render
from .models import Product


def product_list(request):
    top_sale_products = Product.objects.filter(tag=Product.Top_Sale)
    feature_products = Product.objects.filter(tag=Product.Feature)
    new_arrival_products = Product.objects.filter(tag=Product.New_Arrivals)

    context = {
        'top_sale_products': top_sale_products,
        'feature_products': feature_products,
        'new_arrival_products': new_arrival_products,
    }

    return render(request, 'product.html', context)
