from django.shortcuts import render
from product_app.models import Product
from about_app.models import About
from contact_app.models import Contact

def home(request):
    top_sale_products = Product.objects.filter(tag=Product.Top_Sale).order_by('-id')[:3]
    feature_products = Product.objects.filter(tag=Product.Feature).order_by('-id')[:3]
    new_arrival_products = Product.objects.filter(tag=Product.New_Arrivals).order_by('-id')[:3]
    abouts = About.objects.all().order_by('-id')[:2]

    if request.method == 'POST':
        name = request.POST.get('name', '')
        phone_number = request.POST.get('phone_number', '')
        email = request.POST.get('email', '')
        message = request.POST.get('message', '')

        if message:
            Contact.objects.create(
                name=name,
                phone_number=phone_number,
                email=email,
                message=message
            )

    context = {
        'top_sale_products': top_sale_products,
        'feature_products': feature_products,
        'new_arrival_products': new_arrival_products,
        'abouts': abouts,
    }

    return render(request, 'index.html', context)
