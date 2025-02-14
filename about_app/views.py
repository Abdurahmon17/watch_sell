from django.shortcuts import render
from .models import About

def main(request):
    abouts = About.objects.all().order_by('-id')
    context = {'abouts': abouts}

    return render(
        request=request,
        template_name='about.html',
        context=context
    )
