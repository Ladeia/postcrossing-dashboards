from .models import Postcard
from django.shortcuts import render


def index(request):
    postcards = Postcard.objects.all()
    for postcard in postcards:
        setattr(postcard, 'avg', int(postcard.distance.replace(',', '')) / int(postcard.time_travel))

    context = {"postcards": postcards}

    return render(request, 'index.html', context)
