from .models import Postcard
from django.shortcuts import render


def index(request):
    postcards = Postcard.objects.all()
    context = {"postcards": postcards}

    return render(request, 'index.html', context)
