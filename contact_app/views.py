from django.shortcuts import render, redirect
from .models import Contact

def contact_view(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone_number = request.POST.get('phone_number')
        email = request.POST.get('email')
        message = request.POST.get('message')

        Contact.objects.create(
            name=name,
            phone_number=phone_number,
            email=email,
            message=message
        )
        return redirect('success')  # Yuborilganidan keyin muvaffaqiyat sahifasiga o'tadi

    return render(request, template_name='contact.html')
